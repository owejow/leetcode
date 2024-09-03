import unittest

from simple_algorithm.algorithm import Solution as subject
from tests.helpers import expectations


class TestSimpleAlgorithm(unittest.TestCase):
    def test_all(self):
        for k, v in expectations().items():
            nums1, m, nums2, n, expected = (
                v["nums1"],
                v["m"],
                v["nums2"],
                v["n"],
                v["expected"],
            )
            with self.subTest():
                _ = (subject().merge(nums1, m, nums2, n),)
                self.assertEqual(
                    nums1,
                    expected,
                    msg=f"{k} did not match. nums1={nums1}, m={m}, nums2={nums2}, n={n}",
                )
