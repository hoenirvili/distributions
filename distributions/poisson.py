#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

__all__ = ['Poisson']


class Poisson:
    """
        A random variable X that has a Poisson distribution represents 
        the number of events occurring in a fixed time interval with a 
        rate parameters λ. λ tells you the rate at which the number of 
        events occur.  The average and variance is λ.

        Parameters:

        -----------
        n : int 
                Number of events
        rate : int
                The rate that the event occured
    """
    def __init__(self, n,  rate):

        if (type(n) != int or n < 0 or n is None):
            raise ValueError("Invalid number of events")

        if (type(rate) != int or
                rate < 0 or rate is None):
            raise ValueError("Invalid rate number")


        self.__rate = rate
        self.__n = n
        self.__all_n = np.arange(0, n)

    def mean(self):
        """
        Compute the mean of the distribution

        Returns:
        --------

        mean : float

        """
        return poisson.mean(self.__rate)
    
    def variance(self):
        """
        Compute the variance of the distribution

        Returns:
        --------

        variance : float
        """
 
        return poisson.var(self.__rate)

    def std(self):
        """
        Compute the standard deviation of the distribution.

        Returns:
        --------

        std : float
        """
        return poisson.var(self.__rate)

    def pmf(self):
        """
        Compute the probability mass function of the distribution

        Returns:
        --------

        pmf : float
        """
        return poisson.pmf(self.__n, self.__rate)
    
    def pmfs(self):
        """
        Compute the probability mass function of all the elements to n

        Returns:
        --------

        pmf : numpy.narray
        """
 
        return poisson.pmf(self.__all_n, self.__rate)

    def cdf(self):
        """
        Compute the cumulative distribution function.

        Returns:
        --------

        cdf : float
        """

        return poisson.cdf(self.__n, self.__rate)

    def plot(self):
        """Plot values pmfs values of the distribution"""

        pmfs = self.pmfs()
        plt.plot(self.__all_n, pmfs, 'o-')
        plt.title('Poisson: $\lambda$ = %i' % self.__rate)
        plt.xlabel('Number of accidents')
        plt.ylabel('Probability of number of accidents')
        plt.show()


