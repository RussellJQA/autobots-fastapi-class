# Utils Challenge

- Your folder structure should look like the following

```
└── fast-api-class
    ├── .gitignore
    ├── challenges
    │   └── utils_challenge
    │       ├── main.py
    │       ├── tests
    │       │   ├── __init__.py
    │       │   ├── test_math_utils.py
    │       │   └── test_string_utils.py
    │       ├── utils
    │       │   ├── __init__.py
    │       │   ├── math_utils.py
    │       │   └── string_utils.py
    │       └── venv
    ├── python_playground
    │   ├── main.py
    │   ├── tests
    │   │   ├── __init__.py
    │   │   ├── test_json_placeholder.py
    │   │   └── test_math_utils.py
    │   ├── utils
    │   │   ├── __init__.py
    │   │   └── math_utils.py
    │   └── venv
    └── readme.md
```

- Create the following math utilities
  - Add
    - This function will add 2 numbers together
  - Multiply
    - This function will multiply 2 numbers together
- Create the following string utilities
  - string_repeater
    - This function will repeat a string based on the given string and number. For example string_repeater("a", 4) would return "aaaa"
- Inside your `main.py` file print the following things using these new util functions

```
2 + 2 = 4
5 * 5 = 25
Happy Birthday!!!!!!!!!!
```

- Make sure you have a test for each util function
- Make sure your `.gitignore` has the following common things to ignore

```
venv
__pycache__
.pytest_cache
.DS_Store
```

### Requests Extra Credit

- Pick an api from this list and play
  - https://jsonplaceholder.typicode.com/
  - https://github.com/public-apis/public-apis
  - https://github.com/n0shake/Public-APIs