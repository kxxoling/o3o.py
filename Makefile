.PHONY: all test
PACKAGE_NAME = emoticon

all: coverage

test:
	@nosetests

clean: clean-pyc clean-build

clean-build:
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info

clean-pyc:
	@find . -name '*.pyc' -exec rm {} \;
	@find . -name '__pycache__' -type d | xargs rm -rf

make-docs:
	$(MAKE) -C docs html

install:
	@python setup.py install

release: test
	@python setup.py register -r pypi
	@python setup.py sdist upload -r pypi

.PHONY: release clean clean-pyc develop install clean-build

