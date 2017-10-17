#!/usr/bin/env python3

import unittest
import numpy as np
import numpy.testing as numpy_testing
from distributions import Bernoulli

class TestBernoulli(unittest.TestCase):

    def setUp(self):
        self.distribution = Bernoulli(0.70)

    def test_init_with_errors(self):
        params = (
            None, '-3', '3', 
            '-0.2', 'string',
        )

        for param in params:
            with self.assertRaises(ValueError):
                Bernoulli(param)

    def test_mean(self):
        mean = self.distribution.mean()
        self.assertEqual(mean, 0.69999999999999996)

    def test_variance(self):
        variance = self.distribution.variance()
        self.assertEqual(variance, 0.21000000000000002)

    def test_std(self):
        std = self.distribution.std()
        self.assertEqual(std, 0.45825756949558405)

    def test_cdf(self):
        cdf = self.distribution.cdf()
        self.assertEqual(cdf, 1.0)

    def test_pmf(self):
        pmf = self.distribution.pmf()
        self.assertEqual(pmf, 0.0)

    def test_pmfs(self):
        t_pmfs = np.array([ 0.3,  0.7])
        pmfs = self.distribution.pmfs()
        self.assertIsNotNone(pmfs)
        numpy_testing.assert_allclose(t_pmfs, pmfs)
