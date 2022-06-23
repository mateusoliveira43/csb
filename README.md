# csb

[![Continuos Integration](https://github.com/mateusoliveira43/csb/actions/workflows/ci.yml/badge.svg)](https://github.com/mateusoliveira43/csb/actions)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

Technical challenge for selective process.

# Requirements

To run this project, it is necessary the following tools:

- [Docker](https://docs.docker.com/get-docker/) :whale:
- [Docker Compose](https://docs.docker.com/compose/install/) :whale2:

Or

- [Poetry](https://python-poetry.org/docs/#installation) :pencil:

# Quality

To run the project quality measures, run
```
poetry install --no-root
poetry shell
```
if using Poetry, or
```
docker/run.sh
```
then
```
poetry shell
```
in container shell, if using Docker.

To exit Poetry shell, and deactivate virtual environment, run `CTRL+D` or `exit`.

To exit the container's shell, run `CTRL+D` or `exit`.

To run Dockerfile linter, run
```
docker/lint.sh
```

To remove the project's containers, images, volumes and networks, run
```
docker/down.sh
```

To change Docker configuration, change the variables in `.env` file.

Then run the commands presented in each section.

The quality measures of the template are reproduced by the [continuos integration (CI) pipeline](https://github.com/mateusoliveira43/csb/actions) of the project. CI configuration in `.github/workflows/ci.yml` file.

## Tests

To run tests and coverage report, run
```
pytest
```

To see the html report, check `tests/coverage-results/htmlcov/index.html`.

Tests and coverage configuration in `pyproject.toml` file.

## Type checking

To run Python type checker, run
```
mypy .
```

Python type checker configuration in `pyproject.toml` file.

## Linter

To run Python linter, run
```
prospector .
```

Python linter configuration in `.prospector.yaml` file.

## Code formatters

To check Python code imports format, run
```
isort --check --diff .
```

To format Python code imports, run
```
isort .
```

To check Python code format, run
```
black --check --diff .
```

To format Python code, run
```
black .
```

isort and black configuration in `pyproject.toml` file.

To check all repository's files format, run
```
ec -verbose
```

File format configuration in `.editorconfig` file.

## Security vulnerability scanners

To check common security issues in Python code, run
```
bandit --recursive scripts
```

To check known security vulnerabilities in Python dependencies, run
```
safety check --file requirements/dev.txt --full-report
```

# License

This repository is licensed under the terms of [MIT License](LICENSE).
