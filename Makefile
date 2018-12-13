all: setup

setup: virtualenv env pip

virtualenv:
	python3 -m pip install virtualenv

env:
	python3 -m virtualenv env -p python3

pip:
	env/bin/pip install -r requirements.txt

lint:
	env/bin/flake8 oreno_game

run:
	env/bin/python oreno_game/main.py

edit-resource:
	env/bin/pyxeleditor oreno_game/rsc.pyxel