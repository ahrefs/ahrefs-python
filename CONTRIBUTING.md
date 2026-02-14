# Contributing

We welcome bug reports and pull requests.

## Setup

```bash
git clone https://github.com/ahrefs/ahrefs-python.git
cd ahrefs-python
make install
```

## Running checks

```bash
make test      # run unit tests
make lint      # type-check and lint
make format    # auto-format
```

## Pull requests

- Keep changes focused on a single issue or feature.
- Add or update tests for any behavior changes.
- Run `make lint && make test` before submitting.
