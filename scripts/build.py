#!/usr/bin/env python3
"""Build the canonical paper and reject unresolved LaTeX diagnostics."""
import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [ROOT / 'paper' / 'extremes_and_moments_in_greedy_coupon_collection.tex',
           ROOT / 'notes' / 'xu_tang_proof_audit.tex']


def run(*args):
    return subprocess.run(args, cwd=ROOT, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, check=True).stdout


def check_source(source):
    text = source.read_text()
    labels = re.findall(r'\\label\{([^}]+)\}', text)
    assert len(labels) == len(set(labels)), 'Duplicate labels'
    refs = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', text)
    assert not set(refs) - set(labels), 'Undefined source references'
    bib = re.findall(r'\\bibitem\{([^}]+)\}', text)
    assert len(bib) == len(set(bib)), 'Duplicate bibliography keys'
    cites = re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}', text)
    keys = {key.strip() for group in cites for key in group.split(',')}
    assert not keys - set(bib), 'Undefined source citations'
    assert not set(bib) - keys, 'Uncited bibliography entries'
    assert not re.search(r'\\(?:email|affil|orgaddress|orgname|backmatter)\b', text)
    assert not re.search(r'(?i)orcid|cover.letter|sn-jnl|statements and declarations', text)
    assert not re.search(r'[\w.+%-]+@[\w.-]+\.[A-Za-z]{2,}', text), 'Contact address in source'
    print(f'PASS: {len(labels)} unique labels and {len(bib)} cited bibliography entries; clean front matter.')


def build(source, check):
    SOURCE = source
    STEM = source.stem
    PDF = source.with_suffix('.pdf')
    check_source(source)
    with tempfile.TemporaryDirectory(prefix='xu-tang-paper-') as temp:
        env = os.environ.copy()
        env.setdefault('SOURCE_DATE_EPOCH', '1795219200')
        result = subprocess.run(
            ['latexmk', '-pdf', '-halt-on-error', '-interaction=nonstopmode',
             '-no-shell-escape', f'-outdir={temp}', str(SOURCE)],
            cwd=ROOT, env=env, text=True, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        if result.returncode:
            raise RuntimeError(result.stdout[-8000:])
        log = (Path(temp) / (STEM + '.log')).read_text()
        bad = [line for line in log.splitlines() if re.search(
            r'^!|undefined|multiply defined|Overfull|Rerun to get', line)]
        if bad:
            raise RuntimeError('\n'.join(bad))
        built = Path(temp) / (STEM + '.pdf')
        text = run('pdftotext', '-layout', str(built), '-')
        info = run('pdfinfo', str(built))
        if re.search(r'[\w.+%-]+@[\w.-]+\.[A-Za-z]{2,}|(?i:orcid|statements and declarations)', text + info):
            raise RuntimeError('Submission metadata in compiled PDF')
        if check:
            if not PDF.exists() or run('pdftotext', '-layout', str(PDF), '-') != text:
                raise RuntimeError('Committed PDF is missing or differs from rebuilt text; run make pdf')
            print('PASS: committed PDF matches rebuilt text.')
        else:
            shutil.copyfile(built, PDF)
            print(f'Built {PDF.relative_to(ROOT)}')
        print('PASS: no undefined references/citations, duplicate labels, or overfull boxes.')
        print(next(line for line in info.splitlines() if line.startswith('Pages:')))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for source in SOURCES:
        build(source, args.check)
