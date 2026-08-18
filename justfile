# justfile - task runner
#
# usage: just
#

set dotenv-load
set shell := ["bash", "-c"]

# --- Default Command ---

# Lists all tasks (default) same as "just --list"
default:
    @just --list

# --- Trefnu Core Commands ---

# Solve Puzzle
solve-puzzle year day:
    @echo "puzzle year={{ year }} day={{ day }}"
    @uv run python "src/advent/advent{{ year }}/day{{ day }}/puzzle.py"

# --- Testing ---

# Puzzle Test
test year day:
    @echo "test year={{ year }} day={{ day }}"
    @uv run pytest "src/advent/advent{{ year }}/day{{ day }}"
    @uv run behave "./src/advent/advent{{ year }}/day{{ day }}"

# Puzzle Unit Test
test-unit year day:
    @echo "unit test year={{ year }} day={{ day }}"
    @uv run pytest "src/advent/advent{{ year }}/day{{ day }}"

test-unit-year year:
    @echo "unit test year={{ year }}"
    @uv run pytest "src/advent/advent{{ year }}"

# Puzzlue Unit Test All
test-unit-all:
    @echo "unit test all"
    @uv run pytest "src/advent"

# Puzzle Feature Test
test-feature year day:
    @echo "feature test year={{ year }} day={{ day }}"
    @uv run behave "./src/advent/advent{{ year }}/day{{ day }}"

# Feature Test Year
test-feature-year year:
    @echo "feature test year={{ year }}"
    @uv run behave "./src/advent/advent{{ year }}"

# Feature Test All
test-feature-all:
    @echo "feature test all"
    @uv run behave "./src/advent"

# Feature Test All (ignore slow)
test-feature-no-slow:
    @echo "feature test all (ignore slow)"
    @uv run behave "./src/advent" --tags=~@slow

# Analyse Performance
performance year day func="part02":
    @echo "performance year={{ year }} day={{ day }} func={{ func }}"
    @uv run python "src/advent/tools/performance.py" {{ year }} {{ day }} {{ func }}

# Analyse Performance
performance-help:
    @uv run python "src/advent/tools/performance.py" --help
