from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version(distribution_name="ahrefs-python")
except PackageNotFoundError:
    # Fallback for editable installs without metadata — read from pyproject.toml
    __version__ = "0.0.0-dev"
    try:
        from pathlib import Path

        _pyproject = Path(__file__).resolve().parents[2] / "pyproject.toml"
        for _line in _pyproject.read_text().splitlines():
            if _line.startswith("version"):
                __version__ = _line.split('"')[1]
                break
    except Exception:  # noqa: BLE001
        pass
