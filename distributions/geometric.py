#!/usr/bin/env python3


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom
from .distribution import Distribution

__all__ = ['Geometric']


class Geometric(Distribution):
    """
    The geometric distribution is the distribution
    of the number of trials needed to get the first
    sucess in repeated Bernoulli trials.

    Parameters
    ----------
    r : int
        trials needed to get the first success
    p : int or float
        Probability of a trial to be successful
    """

    def __init__(self, r, p):

        if type(r) != int or r < 0 or r is None:
            raise ValueError(
                "Invalid number of trials needed to get the first success")

        if (type(p) != int and type(p) != float or
                p > 1 or p < 0 or p is None):
            raise ValueError("Invalid probability number")

        self.__p = p
        self.__r = r
        self.__not_p = (1 - p)
        self.__all_r = np.arange(0, r + 1)

    def mean(self):
        """
        Compute the mean of the distribution

        Returns:
        --------

        mean : float

        """
        return geom.mean(self.__p)

    def variance(self):
        """
        Compute the variance of the distribution

        Returns:
        --------

        variance : float
        """
        return geom.var(self.__p)

    def pmf(self):
        """
        Compute the probability mass function of the distribution

        Returns:
        --------

        pmf : float
        """
        return geom.pmf(self.__r, self.__p)

    def std(self):
        """
        Compute the standard deviation of the distribution.

        Returns:
        --------

        std : float
        """
        return geom.std(self.__p)

    def cdf(self):
        """
        Compute the cumulative distribution function.

        Returns:
        --------

        cdf : float
        """
        return geom.cdf(self.__r, self.__p)

    def pmfs(self):
        """
        Compute the probability mass function of the distribution of all trials
        needed to get the first success

        Returns:
        --------

        pmf : numpy.narray
        """
        return geom.pmf(self.__all_r, self.__p)

    def plot(self):
        """
        Plot all values pmf values ranging from zero to the
        number of traisl in order to find the first sucess
        """
        pmfs = self.pmfs()
        fix, ax = plt.subplots()
        x = np.arange(0, self.__r + 1)
        plt.bar(x, pmfs, color="blue")
        ax.set_xticks(np.arange(1, len(x)))
        ax.set_title('Geometric distribution')
        ax.set_xlabel('Trials needed to get the first success')
        ax.set_ylabel('Probability')
        plt.show()
