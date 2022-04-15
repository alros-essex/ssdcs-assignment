#!/bin/sh

FOLDER=reports

# cleanup
rm -fr $FOLDER
mkdir $FOLDER

# run coverage
pip3 install pytest
pip3 install pytest-pylint
pip3 install pytest-cov
pytest --cov=my_monit test
coverage report -m
coverage html
rm .coverage
mv htmlcov $FOLDER/cov

# run bandit
pip3 install bandit
bandit --ini .bandit -r > $FOLDER/bandit.txt

# run pylint
pip3 install pylint
pylint --rcfile=pylintrc my_monit > reports/pylint.txt