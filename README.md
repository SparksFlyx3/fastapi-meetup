# SETUP

1. Install [Python](https://www.python.org/)
2. Install [Poetry](https://python-poetry.org/docs/#installation) (Alternative on MacOS: install Poetry via brew)


## 1. Install Python dependencies

```shell
poetry config virtualenvs.in-project true
poetry install
```

Note that Poetry will try to use the default Python version used on your system resulting in the following warning: "The currently activated Python version 3.10.9 is not supported by the project (^3.11). Trying to find and use a compatible version." Poetry will select a different environment matching the required version. To mitigate this warning and set the environment as default, simply run `poetry env use <python-version>` with `<python-version>` either being a version like `3.11` or a path to a specific executable.

## 2. Start application

Open a shell that uses your poetry environment. You can do that by configuring your IDE to use the poetry environment as Interpreter, or run `poetry run` before a Python statement.

```shell
python ./run.py
```

Your application now runs on `http://localhost:8000/api/docs`


## Dependency management

We use [poetry](https://github.com/jazzband/pip-tools) to manage our Python dependencies.

Helpful `poetry` commands:
| Command                                    | Description                                                                                                                                                |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `poetry install`                           | Installs all dependencies, including non-optional groups and creates a poetry.lock file. If a lock file already exists, the locked versions are installed. |
| `poetry install --without foo`             | See `poetry install`, but the group foo is ignored.                                                                                                        |
| `poetry install --with foo`                | See `poetry install`, but additionally installs the group foo (necessary for optional groups).                                                             |
| `poetry add [package-name]`                | Add `package-name` to deployment dependencies                                                                                                              |
| `poetry add --group dev [package-name]`    | Add `package-name` to dev dependencies                                                                                                                     |
| `poetry remove [package-name]`             | Remove `package-name` from deployment dependencies                                                                                                         |
| `poetry remove --group dev [package-name]` | Remove `package-name` from dev dependencies                                                                                                                |
| `poetry update`                            | Update dependencies to the newest versions, lock and install them. Make sure the poetry version used matches the one used in the pipeline.                 |


Direct dependencies of this project are defined in the `[tool.poetry]` sections in [pyproject.toml](pyproject.toml) where the version constraints should be as lenient as possible. Poetry will create a [poetry.lock](poetry.lock) file that locks all direct and indirect  dependencies to a fixed version.

To add/remove/update dependencies use the poetry commands shown above.
This will automatically add the dependency to the pyproject.toml and poetry.lock, as well as install it tn the virtual environment. It is not necessary to re-run `poetry install`.

The current list of dependency groups is specified in pyproject.toml

## Code style

For the following sections, the requirements have to be installed (see above).

### Formatting with ruff and black

To enforce certain coding guidelines and keep the code readable, we use [ruff](https://beta.ruff.rs/docs/)
and [black](https://black.readthedocs.io/en/stable/). To format the code, run:
```sh
ruff check --fix backend
black backend
```

To validate formatting and see what would be changed, run:
```sh
ruff check --diff backend
black backend --check --diff
```

To set up black in your IDE, follow [this tutorial](https://black.readthedocs.io/en/stable/integrations/editors.html).

### Type checks with pyright

To ensure type safety, we use [pyright](https://github.com/microsoft/pyright).
It is installed with the requirements.

Then simply run pyright using:
```sh
pyright
```

Typestubs can be automatically created by using:
```sh
pyright --createstub <import_name>
```
Those stubs are the .pyi files found in /typings and after generation, just represent the stubs of the library. Those stubs can be manipulated to fix missing types.

## Database migrations

The database tables will be created automatically at startup.
The following commands will come in handy:

```sh
alembic upgrade head # upgrade to latest migration
alembic revision --autogenerate -m "insert message here" # autogenerate migration file

alembic upgrade +2 # upgrade two migrations
alembic upgrade ae1bce # upgrade to specific revision by hash
alembic downgrade -2 # downgrade two migrations
alembic current # show current revision hash
```

**Autogenerate takes the current state of the database and migrates it to the current state of the SQLAlchemy models.**

Keep an eye on the content of the autogenerated migration file (!), especially in case of the following: renaming tables or columns, special SQLAlchemy types such as Enum. The resulting files should always be double checked and edited if necessary. All possible migration operations can be found in the [operation reference](https://alembic.sqlalchemy.org/en/latest/ops.html#operation-reference).

Additional information for Alembic can be found in the [documentation](https://alembic.sqlalchemy.org/en/latest/).
