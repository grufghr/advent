ifndef VERBOSE
.SILENT:
endif

puzzle:
	test $(year)
	test $(day)
	./advent$(year)/day$(day)/puzzle.py

test-unit:
	test $(year)
	test $(day)
	python -m unittest discover -v ./advent$(year)/day$(day)

test-unit-year:
	test $(year)
	python -m unittest discover -v ./advent$(year)

test-unit-all:
	python -m unittest discover -v ./

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