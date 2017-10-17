#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from .distribution import Distribution
__all__ = ['Binomial']


class Binomial(Distribution):
    """
    A random variable X that has a bernoulli distribution
    represents one success in one yes/no trial, each of which
    yields success with probability p.

    Parameters
    ----------
    r : int
        Number of successes among n trials
    n : int
        Number of trials
    p : int or float
        Probability of a trial to be successful
    """

    def __init__(self, r, n, p):

        if type(r) != int or r < 0 or r is None:
            raise ValueError("Invalid number of sucesses among n trials")

        if type(n) != int or n < 0 or n is None:
            raise ValueError("Invalid number of trials")

        if (type(p) != int and type(p) != float or
                p > 1 or p < 0 or p is None):
            raise ValueError("Invalid probability number")

        self.__r = r
        self.__n = n
        self.__p = p
        self.__notp = 1 - p
        self.__all_r = np.arange(0, self.__r + 1)

    def mean(self):
        """
        Compute the mean of the distribution

        Returns:
        --------

        mean : float

        """
        return binom.mean(self.__n, self.__p)

    def variance(self):
        """
        Compute the variance of the distribution

        Returns:
        --------

        variance : float
        """
        return binom.var(self.__n, self.__p)

    def pmf(self):
        """
        Compute the probability mass function of the distribution

        Returns:
        --------

        pmf : float
        """
        return binom.pmf(self.__r, self.__n, self.__p)

    def std(self):
        """
        Compute the standard deviation of the distribution.

        Returns:
        --------

        std : float
        """
        return binom.std(self.__n, self.__p)

    def cdf(self):
        """
        Compute the cumulative distribution function.

        Returns:
        --------

        cdf : float
        """
        return binom.cdf(self.__r, self.__n, self.__p)

    def pmfs(self):
        """
        Compute the probability mass function of the distribution of all
        number of successes among n trials [0, r] interval

        Returns:
        --------

        pmf : numpy.narray
        """
        return binom.pmf(self.__all_r, self.__n, self.__p)

    def plot(self):
        """
        Plot all values pmf values ranging from zero to the
        number of successes among n trials
        """
        pmfs = self.pmfs()
        plt.plot(self.__all_r, pmfs, 'o-')
        plt.title('Binomial: number of trials=%i , probability=%.2f' %
                  (self.__n, self.__p), fontsize=15)
        plt.xlabel('Number of successes')
        plt.ylabel('Probability of successes', fontsize=15)
        plt.show()
