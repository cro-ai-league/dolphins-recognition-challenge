.ONESHELL:
SHELL := /bin/bash
SRC = $(wildcard notebooks/*.ipynb)

all: dolphins_recognition_challenge local_install docs

dolphins_recognition_challenge: $(SRC)
	nbdev_build_lib
	touch dolphins_recognition_challenge

local_install: dolphins_recognition_challenge settings.ini
	pip install --user -e .
    
#sync:
#	nbdev_update_lib

docs_serve: docs
	cd docs && bundle exec jekyll serve --host=0.0.0.0

docs: local_install
	nbdev_build_docs
	cd docs; bundle install --path /tmp/vendor/bundle; cd ..
	fix_readme README.md
	touch docs

#	cd docs; bundle install; cd ..

test: local_install
	nbdev_test_nbs --timing True --pause 2 --n_workers 1

release: pypi
#	nbdev_conda_package    
	nbdev_bump_version

pypi: dist
	twine upload --repository pypi dist/*

dist: clean local_install
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist
	touch notebooks/*.ipynb
