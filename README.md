# Simple Flask Application

Simple flask application to simulate slow responses

## Requirements
python3

## Running

**NOTE:** These instructions are assuming that this code will run on a *nix system.

1. (Optional) Create a python virtual environment with the command:
  ```
  python -m venv venv
  ```
  Activate the virtual environment with the command:
  ```
  source venv/bin/activate
  ```
2. Install the required dependencies with the command:
  ```
  pip install -r requirements.txt
  ```
3. Run the development server with the command:
  ```
  python simpleFlask.py
  ```
  The command starts a development server on port 5000



## Adjusting the response delay time

To adjust the response delay time modify the RESPONSE_DELAY variable found in the simpleFlask.py file.