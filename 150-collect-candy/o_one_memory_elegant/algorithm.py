class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype int
        """
        total = len(ratings)
        n = len(ratings) - 1
        peak = 0
        valley = 0
        i = 0

        while i < n:
            while i < n and ratings[i] == ratings[i + 1]:
                i += 1
                peak = 0
                valley = 0

            peak = 0
            while i < n and ratings[i] < ratings[i + 1]:
                i += 1
                peak += 1
                total += peak

            valley = 0
            while i < n and ratings[i] > ratings[i + 1]:
                i += 1
                valley += 1
                total += valley

            total -= min(valley, peak)

        return total
