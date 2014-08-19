#!/usr/bin/env bash

# this script should be run from the CSK_HOME/cato directory, not from the test directory

#set -e

echo "running pylint tests ..."
find . -name "*.py" | xargs pylint --rcfile=test/pylint.conf -E --disable=E0203,E1101,E1103,E0611,E0102,E0702 > test/test_output/pylint.txt
find bin -type f | xargs pylint --rcfile=test/pylint.conf -E --disable=E0203,E1101,E1103,E0611,E0102,E0702 >> test/test_output/pylint.txt

echo "running pep8 tests ..."
pep8 --ignore=W291,E501,W293,E302,E303,E203,E121,W191,E128,E251,E101,E301,E122,E261,E231,E123,E127,W391,E211 . | sed 's/^..//' > test/test_output/pep8.txt
pep8 --ignore=W291,E501,W293,E302,E303,E203,E121,W191,E128,E251,E101,E301,E122,E261,E231,E123,E127,W391,E211 bin/*  >> test/test_output/pep8.txt

echo "command line tests completed"
