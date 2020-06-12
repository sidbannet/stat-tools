"""
Modules for statistical analysis.

@author: siddhartha.banerjee [sidban@uwalumni.com]
"""

import numpy as np


class ProbabilityDensity:
    """
    Class to get probability density.
    """

    def __init__(
            self,
            *args
    ) -> None:
        """Instantiate class."""
        assert len(args) > 0, "Incorrect input format. Input bin sizes."
        for item in args:
            assert type(item) is int, 'Input only integers.'
            assert item > 0, 'Input numbers greater than zero.'
        self._number_of_bins = args
        self._number_of_dims = args.__len__()
