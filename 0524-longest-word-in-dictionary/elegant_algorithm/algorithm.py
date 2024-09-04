class Solution:
    def findLongestWord(self, s, d):
        def isSubsequence(x):
            it = iter(s)
            return all(c in it for c in x)

        d.sort(key=lambda x: (-len(x), x))
        return next(filter(isSubsequence, d), "")
