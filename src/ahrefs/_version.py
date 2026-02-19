from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("ahrefs-python")
except PackageNotFoundError:
    __version__ = "0.2.0"  # fallback for editable installs without metadata
