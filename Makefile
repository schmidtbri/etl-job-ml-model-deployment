TEST_PATH=./

.DEFAULT_GOAL := help

.PHONY: help venv dependencies test-dependencies clean-pyc test

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

venv: ## create virtual environment
	python3 -m venv venv

dependencies: ## install dependencies from requirements.txt
	pip install -r requirements.txt

test-dependencies: ## install dependencies from test_requirements.txt
	pip install -r test_requirements.txt

clean-pyc: ## Remove python artifacts.
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-test:	## Remove test artifacts
	rm -rf .pytest_cache

clean-venv: ## remove all packages from virtual environment
	pip freeze | grep -v "^-e" | xargs pip uninstall -y

test: clean-pyc ## Run unit test suite.
	py.test --verbose --color=yes $(TEST_PATH)
