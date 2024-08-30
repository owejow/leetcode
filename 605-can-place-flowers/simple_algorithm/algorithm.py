class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        items = len(flowerbed)
        final = items - 1
        prev = 0

        for i in range(items):
            if n == 0:
                break
            if (
                prev == 0
                and flowerbed[i] == 0
                and (i == final or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                n -= 1
            prev = flowerbed[i]

        return n == 0
