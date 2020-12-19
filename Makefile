.ONESHELL:
SHELL := /bin/bash
SRC = $(wildcard notebooks/*.ipynb)

all: dolphins_recognition_challenge local_install docs

dolphins_recognition_challenge: $(SRC)
	nbdev_build_lib
	touch dolphins_recognition_challenge

local_install: $(SRC) settings.ini
	pip install -e .
    
sync:
	nbdev_update_lib

docs_serve: docs
	cd docs && bundle exec jekyll serve --host=0.0.0.0

docs: $(SRC)
	nbdev_build_docs
	cd docs; bundle install; cd ..
	touch docs

test:
	nbdev_test_nbs --timing True --pause 2 --n_workers 1

release: pypi
	nbdev_conda_package
	nbdev_bump_version

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist
	touch notebooks/*.ipynb
