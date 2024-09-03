class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
            merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        i = m - 1
        j = m + n - 1
        k = n - 1

        while k >= 0:
            if i < 0:
                nums1[j] = nums2[k]
                k -= 1
                j -= 1
                continue

            a, b = nums1[i], nums2[k]

            if a > b:
                nums1[j] = nums1[i]
                i -= 1
            else:
                nums1[j] = nums2[k]
                k -= 1
            j -= 1
