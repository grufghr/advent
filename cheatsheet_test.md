unit testing
------------

run test suite (disoverable tests)
```
    python -m unittest discover -v
```

run test case
```
    python -m unittest discover ./advent2015/day01 -v
    python -m unittest discover ./advent2022/day03 -v
```

Performance
-----------

find solutions that take more than second, use regex
```
    execution_time = (?!1)
```


