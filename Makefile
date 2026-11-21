.PHONY: pdf verify check

pdf:
	python3 scripts/build.py

verify:
	python3 scripts/verify.py

check:
	python3 scripts/build.py --check
