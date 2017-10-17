#!/usr/bin/env python3

import unittest
import numpy as np
import numpy.testing as numpy_testing
from distributions import Poisson

class TestPoisson(unittest.TestCase):

    def setUp(self):
        self.distribution = Poisson(20, 2)

    def test_init_with_errors(self):
        params = (
            (None, None),
            (1.2, None),
            (-1, None),
            (5, None),
            (5, -2),
            (5, -1.2),
            ('string', 0.85),
            (10, 'some'))

        for param in params:
            with self.assertRaises(ValueError):
                Poisson(*param)

    def test_mean(self):
        mean = self.distribution.mean()
        self.assertEqual(mean, 2.0)

    def test_pmf(self):
        pmf = self.distribution.pmf()
        self.assertEqual(pmf, 5.8329241982692859e-14)

    def test_variance(self):
        variance = self.distribution.variance()
        self.assertEqual(variance, 2.0)

    def test_std(self):
        std = self.distribution.std()
        self.assertEqual(std, 2.0)

    def test_cdf(self):
        cdf = self.distribution.cdf()
        self.assertEqual(cdf, 0.99999999999999389)

    def test_pmfs(self):
        t_pmfs = np.array([  1.35335283e-01,   2.70670566e-01,   2.70670566e-01,
         1.80447044e-01,   9.02235222e-02,   3.60894089e-02,
         1.20298030e-02,   3.43708656e-03,   8.59271640e-04,
         1.90949253e-04,   3.81898506e-05,   6.94360921e-06,
         1.15726820e-06,   1.78041262e-07,   2.54344660e-08,
         3.39126213e-09,   4.23907766e-10,   4.98715019e-11,
         5.54127799e-12,   5.83292420e-13])
        pmfs = self.distribution.pmfs()
        self.assertIsNotNone(pmfs)
  
