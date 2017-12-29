.PHONY: init run test

init:
	pipenv install

run:
	pipenv run pip install --editable .
	pipenv run rebalance-start

test:
	py.test tests
