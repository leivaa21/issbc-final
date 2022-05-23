.PHONY: run deps

SHELL=/bin/zsh

deps:
	@pip install virtualenv
	@python3 -m venv env
	@pip install -r requirements.txt
run:
	@python3 ./main.py