class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        latest = {c: i for i, c in enumerate(s)}
        j = anchor = 0
        partitions = []

        for i, c in enumerate(s):
            j = max(j, latest[c])
            if i == j:
                partitions.append(i - anchor + 1)
                anchor = i + 1
        return partitions


if __name__ == "__main__":
    elems = ["ababcbacadefegdehijhklij"]
    for elem in elems:
        print(elem, Solution().partitionLabels(elem))
