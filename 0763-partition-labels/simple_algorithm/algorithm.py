class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        latest = {c: i for i, c in enumerate(s)}
        anchor = 0
        count = 0
        partitions = []

        for i, c in enumerate(s):
            count += 1
            j = latest[c]
            anchor = max(j, anchor)
            if i == j and j == anchor:
                partitions.append(count)
                count = 0
                anchor += 1
        return partitions


if __name__ == "__main__":
    elems = ["ababcbacadefegdehijhklij"]
    for elem in elems:
        print(elem, Solution().partitionLabels(elem))
