# Project Setup Guide

This guide explains how to set up a Python project environment, install dependencies, create Python files, and run tests using pytest.

## 1. Create a Virtual Environment

First, create a virtual environment in the root directory of the project.

```bash
python -m venv venv
```

## 2. Activate the Virtual Environment

- On **Windows**:

```bash
venv\Scripts\activate
```

- On **MacOS/Linux**:

```bash
source venv/bin/activate
```

## 3. Install Required Packages

```bash
pip install -r requirements.txt
```

## 4. Create Python Files

Create the main Python file and its corresponding test file.

For example:

`sandbox/tdd-simple/addition.py` — the source code

`sandbox/tdd-simple/addition_test.py` — the test file

Example structure:

```bash
tdd-pair-programming/
├── venv/
├── sandbox/
│   ├── tdd-simple/
│   │   ├── addition.py
│   │   └── addition_test.py
│   ├── tdd-mock/
│   │   ├── mock.py
│   │   └── mock_test.py
├── requirements.txt
└── README.md
```

## Run Test Command

```bash
pytest sandbox/ --cov=sandbox --cov-report=html
```