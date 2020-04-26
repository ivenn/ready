class Solution:
    def findMaxLength(self, nums):
        balance = 0
        d = {0: -1}
        longest = 0
        for i, num in enumerate(nums):
            balance += -1 if not num else 1
            if balance in d:
                cur_len = i - d[balance]
                longest = max(cur_len, longest)
            else:
                d[balance] = i

        return longest



def test():
    s = Solution()
    for binarr in ["10010111", "11111", "00000", "101010", "000111"]:
        print(s.findMaxLength([int(i) for i in binarr]))


test()

