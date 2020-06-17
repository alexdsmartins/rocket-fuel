# Rocket-FUEL

Solution for the Advent of Code 2019 - [Day 14 - Space Stoichiometry](https://adventofcode.com/2019/day/14)

## Folder structure

```
├── day14
│   ├── ore.py # functions to run reactions
│   ├── finders.py # successive approximation methods
│   └── tests
└── solution.py # solution for both part I and part II
```

## Setup

1. Create a virtual environment with python>=3.6
2. Install the required modules

```
pip install -r requirements.txt
```

## Running the solution

To run an example run:

```
python solution.py
```

You can also provide a reaction list:

```
python solution.py input.txt
```

## Running the tests

Run pytest on the project root:

```
pytest -v
```
