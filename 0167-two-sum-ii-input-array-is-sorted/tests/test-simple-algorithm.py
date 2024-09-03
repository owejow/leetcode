import unittest

from simple_algorithm.algorithm import Solution as subject
from tests.helpers import expectations


class TestSimpleAlgorithm(unittest.TestCase):
    def test_all(self):
        for k, v in expectations().items():
            numbers, target, expected = v["numbers"], v["target"], v["expected"]
            with self.subTest():
                self.assertEqual(
                    subject().twoSum(numbers, target),
                    expected,
                    msg=f"{k} did not match. numbers={numbers}, target={target}",
                )
