import unittest

from simple_algorithm.algorithm import Solution as subject
from tests.helpers import expectations


class TestSimpleAlgorithm(unittest.TestCase):
    def test_all(self):
        for k, v in expectations().items():
            fb, n, expected = v["flowerbed"], v["n"], v["expected"]
            with self.subTest():
                self.assertEqual(
                    subject().canPlaceFlowers(fb, n),
                    expected,
                    msg=f"{k} did not match. flowerbed={fb}, n={n}",
                )
