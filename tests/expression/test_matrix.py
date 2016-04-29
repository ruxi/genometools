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

"""Tests for the `ExpMatrix` class."""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import str as text

import pytest
import numpy as np

from genometools.expression import ExpMatrix, ExpProfile, ExpGenome


def test_init(my_matrix, my_genes, my_samples, my_X):
    assert isinstance(my_matrix, ExpMatrix)
    assert isinstance(repr(my_matrix), str)
    assert isinstance(str(my_matrix), str)
    assert isinstance(text(my_matrix), text)
    assert isinstance(my_matrix.hash, text)

    assert my_matrix.genes == my_genes
    assert my_matrix.samples == my_samples
    assert np.all(my_matrix.X == my_X)


def test_slice(my_matrix):
    profile = my_matrix.iloc[:, 0]
    assert isinstance(profile, ExpProfile)


def test_transformation(my_matrix):
    other = my_matrix.copy()
    other.center_genes()
    assert np.allclose(other.mean(axis=1), 0.0)
    other = my_matrix.copy()
    other.standardize_genes()
    assert np.allclose(other.std(axis=1, ddof=1), 1.0)


def test_filter(my_matrix, my_genome):
    other = my_matrix.filter_against_genome(my_genome)
    assert other is not my_matrix
    assert other == my_matrix


def test_genome(my_matrix, my_genes):
    genome = my_matrix.get_genome()
    assert isinstance(genome, ExpGenome)
    assert len(genome) == len(my_genes)


def test_copy(my_matrix, my_genes, my_samples, my_X):
    other = my_matrix.copy()
    assert other is not my_matrix
    assert other == my_matrix
    other.genes = my_genes
    other.samples = my_samples
    other.X = my_X
    assert other == my_matrix


def test_tsv(tmpdir, my_matrix):
    output_file = tmpdir.join('expression_matrix.tsv').strpath
    my_matrix.write_tsv(output_file)
    # data = open(str(path), mode='rb').read()
    # h = hashlib.md5(data).hexdigest()
    # assert h == 'd34bf3d376eb613e4fea894f7c9d601f'
    other = ExpMatrix.read_tsv(output_file)
    assert other is not my_matrix
    assert other == my_matrix
