import unittest

from o_one_memory.algorithm import Solution as subject
from tests.helpers import expectations


class TestSimpleAlgorithm(unittest.TestCase):
    def test_all(self):
        for k, v in expectations().items():
            input, expected = v["candies"], v["count"]
            with self.subTest():
                self.assertEqual(
                    subject().candy(input),
                    expected,
                    msg=f"{k} did not match. candies={input}",
                )
