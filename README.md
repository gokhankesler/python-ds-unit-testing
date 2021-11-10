# Data Science Unit Testing
-----------------

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/gokhankesler/python-ds-unit-testing?display_name=0.1.0)](https://github.com/gokhankesler/python-ds-unit-testing)
[![GitHub license](https://img.shields.io/github/license/gokhankesler/python-ds-unit-testing?color=blue&style=flat-square)](https://github.com/gokhankesler/python-ds-unit-testing)
[![Build Status](https://app.travis-ci.com/gokhankesler/python-ds-unit-testing.svg?branch=main)](https://app.travis-ci.com/gokhankesler/python-ds-unit-testing)
[![codecov](https://codecov.io/gh/gokhankesler/python-ds-unit-testing/branch/main/graph/badge.svg?token=ZO9L2Q6WYP)](https://codecov.io/gh/gokhankesler/python-ds-unit-testing)

-----------------
This repo exhibits the example of unit testing practices in a Data Science project.

# Setup
## Configuring the virtual environment.
First of all, let's create a virtual environment not to interfere with your existing python environment.

If it is not installed, first, let's install pip3, the package manager. Use your terminal:

```
sudo pip3 install virtualenv
```

With this command, virtualenv is now installed on our computer. 

You can run the command to check the version.

```
virtualenv --version
```

If all is well, let's continue. We will create the virtual environment with:

```
virtualenv venv 
```
It creates a virtual environment named 'venv'. Next:

```
source venv/bin/activate
```
will activate your virtual environment. It will now be our development environment.

## Installing all dependencies.
Now we will dependencies of the project. 
```
pip install -e .
```


After installing the dependencies, it is ready for use!!!

The folder structure is provided on the following:

```
Main_Project_Folder
├── data/
│  ├── clean/
│  │   ├── clean_housing_data.txt
│  ├── raw/
│      ├── housting_data.txt
├── notebooks/
│   ├── train_test_model.ipynb
├── src/
│   ├── data/
│   │   ├── __init__.py
│   │   ├── preprocessing_helpers.py
│   ├── features/
│   │   ├── __init__.py
│   │   ├── as_numpy.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── train.py
│   ├── visualization/
│   │   ├── __init__.py
│   │   ├── plots.py
│   ├── __init__.py
├── tests/
│   ├── data/
│   │   ├── __init__.py
│   │   ├── test_preprocessing_helpers.py
│   ├── features/
│   │   ├── __init__.py
│   │   ├── test_as_numpy.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── test_train.py
│   ├── visualization/
│   │   ├── __init__.py
│   │   ├── test_plots.py
│   ├── __init__.py
├── .gitignore/
├── .travis.yml
├── LICENCE
├── README.md
├── requirements.txt
├── setup.py
```

