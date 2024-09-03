class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n, 1):
                total = numbers[i] + numbers[j]
                if total == target:
                    return [i + 1, j + 1]
