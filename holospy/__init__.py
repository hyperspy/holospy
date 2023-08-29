from holospy import signals
from holospy import misc
from holospy import datasets

from . import release_info

__all__ = [
    "__version__",
    "datasets",
    "misc",
    "signals",
]


def __dir__():
    return sorted(__all__)


__version__ = release_info.version
__author__ = release_info.author
__copyright__ = release_info.copyright
__license__ = release_info.license
__status__ = release_info.status
