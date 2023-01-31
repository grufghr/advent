ifndef VERBOSE
.SILENT:
endif

# make puzzle year=2016 day=01
puzzle:
	test $(year)
	test $(day)
	./advent$(year)/day$(day)/puzzle.py

# make test year=2016 day=01
test:
	test $(year)
	test $(day)
	python -m unittest discover -v ./advent$(year)/day$(day)

# make test year=2016
test-year:
	test $(year)
	python -m unittest discover -v ./advent$(year)

# make test-all
test-all:
	python -m unittest discover -v ./