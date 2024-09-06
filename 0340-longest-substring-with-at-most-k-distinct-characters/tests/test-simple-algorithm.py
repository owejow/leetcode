import unittest

from simple_algorithm.algorithm import Solution as subject
from tests.helpers import expectations


class TestSimpleAlgorithm(unittest.TestCase):
    def test_all(self):
        for k, v in expectations().items():
            s, u, expected = v["s"], v["k"], v["expected"]
            with self.subTest():
                self.assertEqual(
                    subject().longestSubstring(s, u),
                    expected,
                    msg=f"{k} did not match. s={s}, k={u}",
                )
