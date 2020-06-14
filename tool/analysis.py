"""Statistical analysis module.

This module provides tools for statistical analysis.

NAME
    analysis
CLASSES
    ProbabilityDensity

Typical Usage
==============
::

    from tool.analysis import ProbabilityDensity as Pd
    import matplotlib.pyplot as plt
    pd = Pd(5, 10)
    x, p = pd.pdf(
        data=[[3, 5, 6, 7, 6, 4, ...], [4, 3, 9, 6, 7, 6, ...], ...],
        mass=[1, 2, 1, 3, 2, 1, ...],
    )
    fig = plt.contourf(x[0], x[1], p)

x is the grid of input values
p is the mass weighted probability density of x

@author: siddhartha.banerjee [sidban@uwalumni.com]
"""

from lib.math import multiply as mult
import numpy as np


class ProbabilityDensity:
    """Class to get probability calculation.

    An object to calculate probability density of a continuous variable in
    arbitrary number of dimensions (>= 1).

    Typical Usage - How to Instantiate an object
    ============
    ::
        pd = ProbabilityDensity(number_of_bins_x0, number_of_bins_x1, ...)
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
    ) -> tuple:
        """Return Probability Density.

        Typical Usage
        =============
        ::
            x, p = pd.pdf(
                data=[[3, 5, 6, 7, 6, 4, ...], [4, 3, 9, 6, 7, 6, ...], ...],
                mass=[1, 2, 1, 3, 2, 1, ...],
            )

        :parameter
        data: is a list of [x[i]], where x[i] is a list of data on x_i
        mass: (optional) is the weighted mass of the data

        :returns
        x: numpy.meshgrid containing the mapped x data from all bins
        p: probability density of x in all given dimensions.
        """
        data = np.asarray(data)
        assert data.shape[0] == self._number_of_dims, \
            'Dimension is not matched.'
        if mass is None:
            mass = np.ones_like(data[0])
        else:
            mass = np.asarray(mass)
        x_bins = []
        dx = []
        total_mass = mass.sum()
        idx = np.empty_like(data)
        pdf_o = np.zeros(shape=self._number_of_bins)
        for idim, idata in enumerate(data):
            x_bins.append(
                np.linspace(
                    start=idata.min(),
                    stop=idata.max(),
                    num=self._number_of_bins[idim]
                )
            )
            dx.append(
                (np.ptp(idata)) / (self._number_of_bins[idim])
            )
            idx[idim] = (
                    (
                            idata - idata.min()
                    ) / (
                        np.ptp(idata)
                    ) * (self._number_of_bins[idim] - 1)
            )
        for inum, index in enumerate(idx.T):
            pdf_o[tuple(index.astype(int))] = mass[inum]

        return np.meshgrid(*tuple(x_bins)), \
            pdf_o.T / (total_mass * mult(*tuple(dx)))
