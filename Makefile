.PHONY: all run install lint test coverage

all: install lint test run

run:
	pipenv run python intervals/__init__.py

install:
	pipenv install --dev

lint:
	pipenv run black intervals tests
	pipenv run mypy intervals
	pipenv run flake8 intervals

test:
	pipenv run pytest -vx

coverage:
	pipenv run pytest --cov=intervals --cov-report term-missing tests