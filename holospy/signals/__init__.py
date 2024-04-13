# -*- coding: utf-8 -*-
# Copyright 2016-2023 The holospy developers
#
# This file is part of holospy.
#
# holospy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# holospy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with holospy.  If not, see <http://www.gnu.org/licenses/>.

"""
Modules containing the HoloSpy signals and their lazy counterparts.

HologramImage
    For holography data
LazyHologramImage
    For holography data processed lazily

"""

from .hologram_image import HologramImage, LazyHologramImage

__all__ = [
    "HologramImage",
    "LazyHologramImage",
]


def __dir__():
    return sorted(__all__)
