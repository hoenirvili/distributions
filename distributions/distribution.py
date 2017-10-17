#!/usr/bin/env python3

import abc

__all__ = ['Distribution']


class Distribution(metaclass=abc.ABCMeta):
    """ 
    In probability theory and statistics, a probability distribution 
    is a mathematical function that, stated in simple terms, 
    can be thought of as providing the probabilities of occurrence of 
    different possible outcomes in an experiment
    """

    @abc.abstractmethod
    def mean(self):
        """compute the mean of the distribution"""
        raise NotImplementedError('users must define mean to use this base class')

    @abc.abstractmethod
    def variance(self):
        """compute the variance of the distribution"""
        raise NotImplementedError('users must define variance to use this base class')

    @abc.abstractmethod
    def std(self):
        """compute the standard deviation of the distribution"""
        raise NotImplementedError('users must define std to use this base class')

    @abc.abstractmethod
    def pmf(self):
        """compute the probability mass function of the distribution"""
        raise NotImplementedError('users must define pmf to use this base class')
        pass

    @abc.abstractmethod
    def pmfs(self):
        """compute the probability mass function of all the elements of the distribution"""
        raise NotImplementedError('users must define pmfs to use this base class')

    @abc.abstractmethod
    def cdf(self):
        """compute the cumulative density function of the distribution"""
        raise NotImplementedError('users must define cdf to use this base class')

    @abc.abstractmethod
    def plot(self):
        """plot the distribution of all pmfs"""
        raise NotImplementedError('users must define plot to use this base class')
