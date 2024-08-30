import unittest

from simple_optimized_algorithm.algorithm import Solution as subject
from tests.helpers import expectations


class TestSimpleAlgorithm(unittest.TestCase):
    def test_all(self):
        for k, v in expectations().items():
            s, expected = v["string"], v["expected"]
            with self.subTest():
                self.assertEqual(
                    subject().partitionLabels(s),
                    expected,
                    msg=f"{k} did not match. string={s}",
                )
