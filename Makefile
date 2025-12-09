ifndef VERBOSE
.SILENT:
endif

puzzle:
	test $(year)
	test $(day)
	poetry run python ./advent$(year)/day$(day)/puzzle.py

analyse:
	test $(year)
	test $(day)
	cd ./advent$(year)/day$(day) && ./analyse_performance.py
	
test:
	test $(year)
	test $(day)
	behave ./advent$(year)/day$(day)
	poetry run python -m unittest discover -v ./advent$(year)/day$(day)

test-unit:
	test $(year)
	test $(day)
	poetry run python -m unittest discover -v ./advent$(year)/day$(day)

test-unit-year:
	test $(year)
	poetry run python -m unittest discover -v ./advent$(year)

test-unit-all:
	poetry run python -m unittest discover -v ./

test-feature:
	test $(year)
	test $(day)
	behave ./advent$(year)/day$(day)

test-feature-year:
	test $(year)
	behave ./advent$(year)

test-feature-all:
	behave ./

test-feature-no-slow:
	behave ./ --tags=~@slow