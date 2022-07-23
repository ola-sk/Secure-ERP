# Secure-ERP

Codecool project in which we use Model View Controller design pattern, Clean Code practices and aim for 100% unit test
coverage of code that doesn't directly take the user input.

# The choices

### Python and python package versioning

Because of the point we are in the course, we are not expected yet to implement any sort of virtual environments to
control versioning of Python and python packages. Therefore, we didn't implement it. We may create a list
that present the versions of the packages used by team to run the software successfully. Look for it in the root of the
repo going by a standard name of `requirements.txt`.

# How to Run the app

open erp.py with python 3 in terminal. Depending on your system you may need to use different commands, some options
include:

```
.../Secure-ERP> py ./erp.py
```

```
.../Secure-ERP> python3 ./erp.py
```

```
.../Secure-ERP> python ./erp.py
```

```
.../Secure-ERP> py3 ./erp.py
```

You can run the program providing to python in the command either:

- relational path (like in the examples above), or
- an absolute path, e.g.
    - "/home/example/foo/file.txt" on Linux, or
    - "C:\Users\username\OneDrive - The Organisation\Documents\example\file.txt" on Windows

Remember to surround the path with quotes if it uses spaces.

Use the relational path as in the example above if you start from the project's root directory in the terminal. If you
start from any different directory, and you can relationally navigate to the root of the project where the erp.py file
resides, the relational call is also possible.

From any directory on your system you can call the python to run the erp.py providing the absolute path to the erp.py
file.

# Unit tests

Unit tests use the pytest module to run the unit tests. In the root directory of the project you can find the
pytest.ini, which is the configuration file for the pytest. If you run the pytest from terminal being in that root
directory of the project, the pytest should automatically detect the configuration file and use it. The `pytest.ini`
specifies the minimum version of pytest that should run the tests by setting the `minversion = 7.1`, which in this case
specifies the minimal version to be 7.1.
`addopts` variable sets the flags/arguments that the pytest is being run with, e.g. `addopts = -ra` tells the pytest to
report all tests.
`testpaths` tells pytest where to find the tests relational to the root directory (in which the pytest.ini is placed).
Test paths can be separated by a new line in the `pytest.ini` file, like:

```
testpaths =
    tests
    integration
```

## How to Run the unit tests

To run the unit tests, you first need to have pytest installed. Then from the terminal, if needed, first change the 
directory to the root of the "Secure-ERP" project. Then, depending on your system, and its configuration with the python 
ecosystem, you can either run pytest using the `pytest` command directly or first calling python in your terminal, e.g.
`py`/`py3`/`python`/`python3` etc. with a flag `-m` and providing package name `pytest`, which in result looks like:

```
py -m pytest
```

pytest should detect the `pytest.ini` configuration file that is in the root of the project and set up the test
accordingly. According to the configuration file it should start looking in the `./tests` directory for tests to be run.