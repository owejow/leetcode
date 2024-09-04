import math


class Solution:
    def judgeSquareSum(self, c):
        """
        c: int -> bool
        """
        s = 0
        e = int(math.isqrt(c))
        while s <= e:
            candidate = s * s + e * e
            if candidate == c:
                return True
            elif candidate < c:
                s += 1
            else:
                e -= 1
        return False
