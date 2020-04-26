class Solution:
    def singleNumber(self, nums):
        res = nums.pop(0)

        while nums:
            res ^= nums.pop(0)

        return res