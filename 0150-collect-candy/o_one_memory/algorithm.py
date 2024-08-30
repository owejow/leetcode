class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype int
        """
        total = 0
        for segment in Solution.segments(ratings):
            total += Solution.total(*segment)
        return total

    @staticmethod
    def total(prev, cur, n, adjustment=0):
        if cur == 0:
            return n
        elif prev == -1 and cur == 1:
            return (n + 1) * (n + 2) / 2 - 1
        elif prev == 1 and cur == -1:
            return n * (n + 1) / 2 + adjustment
        else:
            return (n) * (n + 1) / 2

    @staticmethod
    def segments(ratings):
        pp_m = 0
        p_m = 0
        c_m = 0
        c_c = 0
        p_c = 0
        n = len(ratings)
        for i in range(n):
            if i == n - 1:
                c_c += 1
                yield (
                    p_m,
                    c_m,
                    c_c,
                    Solution.adjustment(pp_m, p_m, c_m, p_c, c_c),
                )
                break

            m = Solution.slope(ratings[i], ratings[i + 1])
            s_change = c_m != m

            if s_change:
                if c_m == 0:
                    yield (p_m, c_m, c_c, 0)
                    p_c = c_c
                    # push last equal to next interval
                    c_c = 1
                else:
                    # include equal in current interval
                    c_c += 1
                    yield (
                        p_m,
                        c_m,
                        c_c,
                        Solution.adjustment(pp_m, p_m, c_m, p_c, c_c),
                    )
                    p_c = c_c
                    c_c = 0

                pp_m = p_m
                p_m = c_m
                c_m = m
            else:
                c_c += 1

        yield (0, 0, 0, 0)

    @staticmethod
    def adjustment(pp_m, p_m, c_m, p_c, c_c):
        if p_m == 1 and c_m == -1:
            if pp_m == -1:
                return max(c_c - p_c, 0)
            else:
                return max(c_c - p_c + 1, 0)
        return 0

    @staticmethod
    def slope(a, b):
        if a == b:
            return 0
        elif a > b:
            return -1
        else:
            return 1
