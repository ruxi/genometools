# Copyright (c) 2016 Florian Wagner
#
# This file is part of GenomeTools.
#
# GenomeTools is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License, Version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Tests for functions in `cluster` module."""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import str as text

import numpy as np

from genometools.expression import cluster, ExpMatrix


def test_init(my_matrix):
    clust, a, b = cluster.bicluster(my_matrix)
    assert isinstance(clust, ExpMatrix)
    assert isinstance(a, np.ndarray)
    assert isinstance(b, np.ndarray)