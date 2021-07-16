![GitHub](https://img.shields.io/github/license/FRReinert/accapi)
![GitHub last commit](https://img.shields.io/github/last-commit/FRReinert/accapi)

![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/FRReinert/accapi/fastapi)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/FRReinert/accapi/pydantic)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/FRReinert/accapi/uvicorn)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/FRReinert/accapi/firebase-admin)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/FRReinert/accapi/pytest)

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