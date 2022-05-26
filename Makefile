.PHONY: run run_cli deps

SHELL=/bin/zsh

deps:
	@pip install virtualenv
	@python3 -m venv env
	@pip install -r requirements.txt
run:
	@python3 ./src/main.py

run_cli:
	@python3 ./src/main_cli.py
