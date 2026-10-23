# TODO list (Django)

A simple task list: add, check off and delete items.

> Status: minimal runnable version. Parts that were incomplete are marked with `TODO` in the code; external services are mocked.

## Quick start (Docker)

```sh
make docker-run        # builds the image and serves http://localhost:8000
```

## Quick start (local Python 3.7)

```sh
make setup             # creates .venv and installs requirements.txt
make run               # migrates SQLite and serves http://localhost:8000
make superuser         # optional: admin user for /admin
```

## Mocks

Controlled by `USE_MOCKS` (default `1`), added at the end of `todo_list/settings.py`:

- No external services. Uses SQLite.

## TODO

- None found beyond the mocks above.
- TODO: move `SECRET_KEY` out of source control before any deployment.
