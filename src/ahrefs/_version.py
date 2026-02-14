from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("ahrefs-python")
except PackageNotFoundError:
    __version__ = "0.1.0"  # fallback for editable installs without metadata
