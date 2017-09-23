help:
	@echo "help..."
	@exit 1

files_tests = $(shell find tests/ -iname '*.py' -type f)
files_prog = $(shell find ppgr/ -iname '*.py' -type f)
files_rest = setup.py
files_all = $(files_prog) $(files_tests) $(files_rest)

publish: test
	@scripts/publish

# --- TESTS ---

test: test-pytest test-flake8 test-isort

test-pytest:
	pipenv run -- pytest $(files_tests)

test-flake8:
	pipenv run -- flake8 $(files_all)

test-isort:
	pipenv run -- isort --check-only --line-width 119 $(files_all)

coverage:
	pipenv run -- pytest --cov=ppgr $(files_tests)

isort:
	pipenv run -- isort --apply --line-width 119 $(files_all)

# --- CLEAN ---

.PHONY: clean
clean:
	find . -iname '*.pyc' -type f -delete
	rm -f README
