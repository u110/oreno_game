all: setup

setup: virtualenv pip

virtualenv:
	python -m virtualenv env -p python3

pip:
	env/bin/pip install -r requirements.txt
