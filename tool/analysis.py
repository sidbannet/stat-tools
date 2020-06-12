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

    def pdf(
            self,
            data: list = None,
            mass: list = None,
    ) -> np.ndarray:
        """Return Probability Density."""
        data = np.asarray(data)
        assert data.shape[0] == self._number_of_dims, \
            'Dimension is not matched.'
        if mass is None:
            mass = np.ones_like(data[0])
        else:
            mass = np.asarray(mass)
        x_bins = []
        total_mass = mass.sum()
        idx = np.empty_like(data)
        PDFo = np.zeros(shape=self._number_of_bins)
        for idim, idata in enumerate(data):
            x_bins.append(
                np.linspace(
                    start=idata.min(),
                    stop=idata.max(),
                    num=self._number_of_bins[idim]
                )
            )
            idx[idim] = (
                (
                        idata - idata.min()
                ) / (
                        np.ptp(idata)
                ) * (self._number_of_bins[idim] - 1)
            )
        for inum, index in enumerate(idx.T):
            PDFo[tuple(index.astype(int))] = mass[inum]

        return PDFo / total_mass
