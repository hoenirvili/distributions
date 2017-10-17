#!/usr/bin/env python3

import unittest
import numpy as np
import numpy.testing as numpy_testing
from distributions import Binomial


class TestBinomail(unittest.TestCase):

    def setUp(self):
        self.distribution = Binomial(3, 5, 0.85)

    def test_init_with_errors(self):
        params = (
            (None, None, None),
            (1.2, None, None),
            (-1, None, None),
            (-1.2, None, None),
            (3, None, None),
            (3, 1.2, None),
            (3, -1, None),
            (3, 5, None),
            (3, 5, -2),
            (3, 5, -1.2),
            ('some', 5, 0.85),
            (5, 'string', 0.85),
            (5, 10, 'some'),
            (3, 5, 2))

        for param in params:
            with self.assertRaises(ValueError):
                Binomial(*param)

    def test_mean(self):
        mean = self.distribution.mean()
        self.assertEqual(mean, 4.25)

    def test_pmf(self):
        pmf = self.distribution.pmf()
        self.assertEqual(pmf, 0.13817812500000001)

    def test_variance(self):
        variance = self.distribution.variance()
        self.assertEqual(variance, 0.63750000000000007)

    def test_std(self):
        std = self.distribution.std()
        self.assertTrue(std, 0.79843597113356568)

    def test_cdf(self):
        cdf = self.distribution.cdf()
        self.assertTrue(cdf, 0.16479000000000005)

    def test_pmfs(self):
        t_pmfs = np.array([7.59375000e-05, 2.15156250e-03, 2.43843750e-02, 1.38178125e-01])
        pmfs = self.distribution.pmfs()
        self.assertIsNotNone(pmfs)
        numpy_testing.assert_allclose(t_pmfs, pmfs)
