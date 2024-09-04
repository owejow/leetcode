class Solution:
    def checkPossibility(self, nums):
        count = 0
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if count > 1:
                    return False
                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
        return True
