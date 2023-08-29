from . import datasets, release_info, signals, reconstruct, tools

__all__ = [
    "__version__",
    "datasets",
    "signals",
    "reconstruct",
    "tools",
]


def __dir__():
    return sorted(__all__)


__version__ = release_info.version
__author__ = release_info.author
__copyright__ = release_info.copyright
__license__ = release_info.license
__status__ = release_info.status
