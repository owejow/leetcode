from collections import defaultdict


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or k == 0:
            return 0

        i = 0
        j = 0
        char_counts = defaultdict(lambda: 0)
        char_counts[s[i]] += 1
        distinct_chars = 1
        size = 1
        max_size = 1

        while j < len(s):
            if distinct_chars > k:
                char_counts[s[i]] -= 1
                if char_counts[s[i]] == 0:
                    distinct_chars -= 1
                size -= 1

                if i == j:
                    j += 1
                    if j < len(s):
                        if char_counts[s[j]] == 0:
                            distinct_chars += 1
                        char_counts[s[j]] += 1
                        size += 1
                        if distinct_chars < k and size > max_size:
                            max_size = size
                i += 1
            else:
                j += 1
                if j < len(s):
                    if char_counts[s[j]] == 0:
                        distinct_chars += 1
                    char_counts[s[j]] += 1
                    size += 1
                    if distinct_chars <= k:
                        if size > max_size:
                            max_size = size
        return max_size
