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

"""Tests for the `GSEAnalysis` class."""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import str as text

from string import ascii_lowercase

import pytest

# from genometools.expression import ExpGenome
from genometools import misc
from genometools.enrichment import GSEAnalysis

logger = misc.get_logger('genometools', verbose=True)


@pytest.fixture
def my_analysis(my_genome, my_gene_set_db):
    analysis = GSEAnalysis(my_genome, my_gene_set_db)
    return analysis


def test_init(my_analysis, my_genome):
    assert isinstance(my_analysis, GSEAnalysis)
    assert isinstance(repr(my_analysis), str)
    assert isinstance(str(my_analysis), str)
    assert isinstance(text(my_analysis), text)

    assert isinstance(my_analysis.genes, list)
    assert len(my_analysis.genes) == len(my_genome)

def test_analysis(my_analysis, my_ranked_genes, my_uninteresting_gene_set):
    pval_thresh = 0.025
    X_frac = 0
    X_min = 1
    L = len(my_ranked_genes)
    enriched = my_analysis.get_enriched_gene_sets(
        my_ranked_genes, pval_thresh, X_frac, X_min, L)
    assert isinstance(enriched, list)
    assert len(enriched) == 1

    enriched = my_analysis.get_enriched_gene_sets(
        my_ranked_genes, pval_thresh, X_frac, X_min, L,
        gene_set_ids=[my_uninteresting_gene_set.id])
    assert isinstance(enriched, list)
    assert len(enriched) == 0