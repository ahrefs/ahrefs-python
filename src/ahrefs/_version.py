from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("ahrefs-python")
except PackageNotFoundError:
    __version__ = "0.3.1"  # fallback for editable installs without metadata
