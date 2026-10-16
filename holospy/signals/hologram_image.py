# Copyright 2007-2026 The HyperSpy developers
#
# This file is part of HyperSpy.
#
# HyperSpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HyperSpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HyperSpy. If not, see <https://www.gnu.org/licenses/#GPL>.
import warnings

from hyperspy.exceptions import VisibleDeprecationWarning

# ruff: noqa: F822

__all__ = ["HologramImage", "LazyHologramImage"]


def __dir__():
    return sorted(__all__)


def __getattr__(name):
    warnings.warn(
        "This module has been privatised, use `holospy.signals` instead. "
        "It will be removed in holospy 1.0.",
        VisibleDeprecationWarning,
    )

    if name == "HologramImage":
        from ._hologram_image import HologramImage

        return HologramImage
    elif name == "LazyHologramImage":
        from ._lazy_hologram_image import LazyHologramImage

        return LazyHologramImage
    else:
        raise AttributeError(f"module {__name__} has no attribute {name}")
