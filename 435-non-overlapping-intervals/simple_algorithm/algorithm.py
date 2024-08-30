class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])
        target = float("-inf")
        count = 0

        for interval in intervals:
            if interval[0] >= target:
                target = interval[1]
            else:
                count += 1

        return count
