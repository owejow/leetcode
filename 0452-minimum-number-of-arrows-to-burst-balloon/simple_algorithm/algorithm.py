class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points.sort(key=lambda x: x[1])

        arrows = 0
        test = float("-inf")

        for p in points:
            if p[0] > test:
                arrows += 1
                test = p[1]

        return arrows
