import unittest

from simple_algorithm.algorithm import Solution as subject
from tests.helpers import expectations


class TestSimpleAlgorithm(unittest.TestCase):
    def test_all(self):
        for k, v in expectations().items():
            prices, expected = v["prices"], v["expected"]
            with self.subTest():
                self.assertEqual(
                    subject().maxProfit(prices),
                    expected,
                    msg=f"{k} did not match. prices={prices}",
                )
