class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        nullp = 0

        while nullp < len(nums)-1 and p < len(nums)-1:
            while nums[nullp] != 0 and nullp < len(nums)-1:
                nullp += 1
            while nums[p] == 0 and p < len(nums)-1:
                p += 1
            if nullp < p:
                nums[p], nums[nullp] = nums[nullp], nums[p]
            else:
                p += 1

    def moveZeroes2(self, nums):
        none_zero = 0
        cur = 0

        while cur < len(nums):
            if nums[cur] != 0:
                nums[none_zero], nums[cur] = nums[cur], nums[none_zero]
                none_zero += 1
            cur += 1

def test():
    l = [0,1,0,3,12]
    l = [0,0,0,0,0]
    l= [1,1,1,1,1]
    l = [0,0,0,1,1,1]
    l = [1,0,1]
    Solution().moveZeroes2(l)
    print(l)

test()