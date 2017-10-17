#!/usr/bin/env python3

import unittest
import numpy as np
import numpy.testing as numpy_testing
from distributions import Geometric


class TestGeometric(unittest.TestCase):

    def setUp(self):
        self.distribution = Geometric(10, 0.85)

    def test_init_with_errors(self):
        params = (
            (None, None),
            (1.2, None),
            (-1, None),
            (5, None),
            (5, -2),
            (5, -1.2),
            ('string', 0.85),
            (10, 'some'),
            (5, 2))

        for param in params:
            with self.assertRaises(ValueError):
                Geometric(*param)

    def test_mean(self):
        mean = self.distribution.mean()
        self.assertEqual(mean, 1.1764705882352942)

    def test_pmf(self):
        pmf = self.distribution.pmf()
        self.assertEqual(pmf, 3.2676855468750044e-08)

    def test_variance(self):
        variance = self.distribution.variance()
        self.assertEqual(variance, 0.20761245674740489)

    def test_std(self):
        std = self.distribution.std()
        self.assertEqual(std, 0.45564509955381383)

    def test_cdf(self):
        cdf = self.distribution.cdf()
        self.assertEqual(cdf, 0.99999999423349606)

    def test_pmfs(self):
        t_pmfs = np.array([  0.00000000e+00,   8.50000000e-01,   1.27500000e-01,
         1.91250000e-02,   2.86875000e-03,   4.30312500e-04,
         6.45468750e-05,   9.68203125e-06,   1.45230469e-06,
         2.17845703e-07,   3.26768555e-08])
        pmfs = self.distribution.pmfs()
        self.assertIsNotNone(pmfs)
        numpy_testing.assert_allclose(t_pmfs, pmfs)
