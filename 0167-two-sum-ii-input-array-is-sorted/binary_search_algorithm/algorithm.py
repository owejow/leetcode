class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)
        for i in range(n - 1):
            left = i + 1
            right = len(numbers) - 1

            value = target - numbers[i]

            while left <= right:
                m = (left + right) // 2
                c = numbers[m]
                if c == value:
                    return [i + 1, m + 1]
                elif c > value:
                    right = m - 1
                else:
                    left = m + 1
