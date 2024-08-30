class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        intervals = Solution.letter_intervals(s)
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        result = []

        prev = intervals[0][1]
        for i in range(1, n):
            if prev < intervals[i][0]:
                result.append(prev)
            prev = max(prev, intervals[i][1])

        if len(result) == 0:
            return [len(s)]

        pv = 0
        lengths = []

        for i, elem in enumerate(result):
            if i == 0:
                lengths.append(elem - pv + 1)
            else:
                lengths.append(elem - pv)
            pv = elem
        lengths.append(len(s) - result[-1] - 1)

        return lengths

    @staticmethod
    def letter_intervals(string):
        start_intervals = [float("-inf")] * 26
        stop_intervals = [float("-inf")] * 26
        for i, char in enumerate(string):
            idx = ord(char) - 97
            if start_intervals[idx] >= 0:
                stop_intervals[idx] = i
            else:
                start_intervals[idx] = i
                stop_intervals[idx] = i
        return [elem for elem in zip(start_intervals, stop_intervals) if elem[0] >= 0]
