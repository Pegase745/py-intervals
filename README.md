# py-intervals

![Screenshot](/screenshot.png)
[![Build Status](https://travis-ci.com/Pegase745/py-intervals.svg?branch=master)](https://travis-ci.com/Pegase745/py-intervals)
[![codecov](https://codecov.io/gh/Pegase745/py-intervals/branch/master/graph/badge.svg)](https://codecov.io/gh/Pegase745/py-intervals)


**Requirements**

* Python >= 3.7

**Dev requirements**

* [Pipenv](https://github.com/pypa/pipenv#installation)

## Usage

```
$ python intervals/__init__.py
```

## Usage using Makefile

* `make install`: Install development dependencies (requires Pipenv)
* `make run`: Runs main program
* `make lint`: Runs formatter, type checker and linter
* `make test`: Runs test suite
* `make coverage`: Runs test suite and report coverage percentage
* `make all`: Runs `install`, `lint`, `test`, `run`