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

"""Heat map annotation classes.

"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

import logging

import numpy as np

logger = logging.getLogger(__name__)


class HeatmapItemAnnotation(object):

    default_transparency = 0.3

    # TODO: docstrings, __str__, __repr__, ...

    def __init__(self, key, color, **kwargs):

        label = kwargs.pop('label', None)
        transparency = kwargs.pop('transparency', self.default_transparency)

        # key can be anything allowed as a key in a pandas index.
        assert isinstance(color, str)
        if label is not None:
            assert isinstance(label, str)
        if transparency is not None:
            assert isinstance(transparency, (int, float))

        self.key = key
        self.color = color
        self.label = label
        self.transparency = transparency


class HeatmapGeneAnnotation(HeatmapItemAnnotation):

    # TODO: docstrings, __str__, __repr__, ...

    def __init__(self, gene, color, **kwargs):
        HeatmapItemAnnotation.__init__(self, gene, color, **kwargs)

    @property
    def gene(self):
        """Alias for `HeatmapItemAnnotation.key`."""
        return self.key

    @gene.setter
    def gene(self, value):
        self.key = value


class HeatmapSampleAnnotation(HeatmapItemAnnotation):

    # TODO: docstrings, __str__, __repr__, ...

    def __init__(self, sample, color, **kwargs):
        HeatmapItemAnnotation.__init__(self, sample, color, **kwargs)

    @property
    def sample(self):
        """Alias for `HeatmapItemAnnotation.key`."""
        return self.key

    @sample.setter
    def sample(self, value):
        self.key = value


class HeatmapBlockAnnotation(object):

    # TODO: docstrings, __str__, __repr__, ...

    def __init__(self, start_index, end_index, **kwargs):

        label = kwargs.pop('label', None)
        color = kwargs.pop('color', 'black')
        transparency = kwargs.pop('transparency', 0.3)

        # key can be anything allowed as a key in a pandas index.
        assert isinstance(start_index, (int, np.integer))
        assert isinstance(end_index, (int, np.integer))
        assert isinstance(color, str)
        if label is not None:
            assert isinstance(label, str)
        assert isinstance(transparency, (int, float, np.integer, np.float))

        self.start_index = start_index
        self.end_index = end_index
        self.color = color
        self.label = label
        self.transparency = transparency
