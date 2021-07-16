## Prepare environment

```sh
# Install pipenv
$ accpi> pip install pipenv

# Initialize virtual environment and install dependencies
$ accpi> pipenv shell && pipenv install
```

## Run Tests

```sh
# Initialize virtual environment
$ accpi> pipenv shell

# Run Tests
$ accpi> pytest
```

## Run local application

```sh
$ accpi> uvicorn account_api.main:app --reload 
````