# Copyright 2016-2026 The holospy developers
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
# along with holospy.  If not, see <https://www.gnu.org/licenses/>.

import pytest
from hyperspy.exceptions import VisibleDeprecationWarning


def test_import_privatised_signals():
    with pytest.warns(VisibleDeprecationWarning) as record:
        from holospy.signals.hologram_image import (  # noqa: F401
            HologramImage,
            LazyHologramImage,
        )

    assert "use `holospy.signals` instead" in record[0].message.args[0]
