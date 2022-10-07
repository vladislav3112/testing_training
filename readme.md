## How to run tests:
### 1. run doctests for morse.py: 
* python -m doctest -v morse.py
### 2. run pytests for morse.py: 
* python -m pytest -v morse.py
### 3. run unittests for one_hot_encoder.py: 
* python -m unittest one_hot_encoder.py  
### 4. run pytests for one_hot_encoder.py: 
* python -m pytest one_hot_encoder.py
### 5. run coverage + pytests for test_what_is_year_now.py: 
* python -m pytest --cov=what_is_year_now --cov-report html