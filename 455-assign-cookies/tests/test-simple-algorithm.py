import unittest

from simple_algorithm.algorithm import Solution as subject
from tests.helpers import expectations


class TestSimpleAlgorithm(unittest.TestCase):
    def test_all(self):
        for k, v in expectations().items():
            g, s, expected = v["greed"], v["size"], v["expected"]
            with self.subTest():
                self.assertEqual(
                    subject().findContentChildren(g, s),
                    expected,
                    msg=f"{k} did not match. greed={g}, size={s}",
                )
