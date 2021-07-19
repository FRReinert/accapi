![GitHub](https://img.shields.io/github/license/FRReinert/accapi)
![GitHub last commit](https://img.shields.io/github/last-commit/FRReinert/accapi)

![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/FRReinert/accapi/fastapi)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/FRReinert/accapi/pydantic)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/FRReinert/accapi/uvicorn)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/FRReinert/accapi/firebase-admin)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/FRReinert/accapi/pytest)

## Prepare environment

```sh
# Set environment variables
ACCAPI_G_DEBUG=true
ACCAPI_G_CERTIFICATE=path/to/cert.json
ACCAPI_G_PROJECT_ID=GAEPROJID
ACCAPI_USERNAME=myuser
ACCAPI_PASSWORD=mypaswd

# Install pipenv
$ pip install pipenv

# Initialize virtual environment and install dependencies
$ pipenv shell && pipenv install
```

## Run Tests

```sh
# Initialize virtual environment
$ pipenv shell

# Run Tests
$ pytest
```

## Run local application

```sh
$ uvicorn account_api.main:app --reload 
````