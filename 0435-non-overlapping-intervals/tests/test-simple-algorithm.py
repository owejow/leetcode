import unittest

from simple_algorithm.algorithm import Solution as subject
from tests.helpers import expectations


class TestSimpleAlgorithm(unittest.TestCase):
    def test_all(self):
        for k, v in expectations().items():
            i, expected = v["intervals"], v["expected"]
            with self.subTest():
                self.assertEqual(
                    subject().eraseOverlapIntervals(i),
                    expected,
                    msg=f"{k} did not match. interval={i}",
                )
