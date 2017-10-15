#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli


__all__ = ['Bernoulli']


class Bernoulli:
    """
    A random variable X that has a bernoulli distribution
    represents the success in one
    independent yes/no trial, of which
    yields success with probability of p.

    Parameters

    ----------
    p : int or float
        Probability of a trial to be successful
    """

    def __init__(self, p):

        if (type(p) != int and type(p) != float or
                p > 1 or p < 0 or p is None):
            raise ValueError("Invalid probability number")

        self.__p = p
        self.__r = 2
        self.__all_r = np.arange(0, self.__r)

    def mean(self):
        """
        Compute the mean of the distribution

        Returns:
        --------

        mean : float

        """
        return bernoulli.mean(self.__p)

    def variance(self):
        """
        Compute the variance of the distribution

        Returns:
        --------

        variance : float
        """
        return bernoulli.var(self.__p)

    def std(self):
        """
        Compute the standard deviation of the distribution.

        Returns:
        --------

        std : float
        """
        return bernoulli.std(self.__p)

    def pmf(self):
        """
        Compute the probability mass function of the distribution

        Returns:
        --------

        pmf : float
        """
        return bernoulli.pmf(self.__r, self.__p)

    def cdf(self):
        """
        Compute the cumulative distribution function.

        Returns:
        --------

        cdf : float
        """
        return bernoulli.cdf(self.__r, self.__p)

    def pmfs(self):
        """
        Compute the probability mass function of the distribution the
        success and failure in one trial p, 1-p

        Returns:
        --------

        pmf : numpy.narray
        """
        return bernoulli.pmf(self.__all_r, self.__p)

    def plot(self):
        """Plot values pmfs values of the distribution in one trial"""

        pmfs = self.pmfs()
        fix, ax = plt.subplots()
        x = np.arange(0, 2)
        plt.bar(x, pmfs, color="blue")
        ax.set_xticks(x)
        ax.set_xticklabels(['Failure', 'Success'])
        ax.set_title('Bernoulli distribution')
        ax.set_ylabel('Probability of success')
        ax.set_ylim([0, 1])
        plt.show()
