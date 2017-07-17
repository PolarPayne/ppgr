help:
	@echo "help..."
	@exit 1

bin ?= venv/bin

files_tests = $(shell find tests/ -iname '*.py' -type f)
files_prog = $(shell find ppgr/ -iname '*.py' -type f)
files_rest = setup.py
files_all = $(files_prog) $(files_tests) $(files_rest)

publish: test
	@bin='$(bin)' scripts/publish

# --- TESTS ---

test: test-pytest test-flake8 test-isort

test-pytest: venv
	$(bin)/pytest $(files_tests)

test-flake8: venv
	$(bin)/flake8 setup.py $(files_all)

test-isort: venv
	$(bin)/isort --check-only --line-width 119 $(files_all)

coverage: venv
	$(bin)/pytest --cov=ppgr $(files_tests)

isort: venv
	$(bin)/isort --apply --line-width 119 $(files_all)

# --- VENV ---

venv: venv/bin/activate
venv/bin/activate: requirements_dev.txt
	test -d venv || python3 -m venv venv
	$(bin)/pip install -Ur $?
	touch $@

# --- CLEAN ---

.PHONY: clean
clean:
	find . -iname '*.pyc' -type f -delete
	rm -f README

clean-all: clean
	rm -rf venv
