class Solution:
    def maxSubArray(self, nums):
        res = [nums[0]]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            res.append(max(res[i-1]+nums[i], nums[i]))
            max_sum = max(max_sum, res[i])

        return max_sum


def test():
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


test()
