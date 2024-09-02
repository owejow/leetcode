import unittest

from simple_algorithm.algorithm import Solution as subject
from tests.helpers import expectations


class TestSimpleAlgorithm(unittest.TestCase):
    def test_all(self):
        for k, v in expectations().items():
            nums, expected = v["nums"], v["expected"]
            with self.subTest():
                self.assertEqual(
                    subject().checkPossibility(nums),
                    expected,
                    msg=f"{k} did not match. nums={nums}",
                )
