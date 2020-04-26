class Solution:
    def productExceptSelf(self, nums):
        if len(nums) == 1:
            return nums

        prod = [1 for _ in nums]

        tmp = 1
        for i in range(len(nums)):
            prod[i] = tmp
            tmp *= nums[i]

        tmp = 1
        for i in range(len(nums)-1, -1, -1):
            prod[i] *= tmp
            tmp *= nums[i]

        return prod


def test():
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))


test()