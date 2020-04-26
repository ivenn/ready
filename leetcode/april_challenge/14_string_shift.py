class Solution:
    def stringShift(self, s, shift):
        balance = sum([-num if dir == 0 else num
                       for dir, num in shift])

        if balance > 0:   # right
            balance %= len(s)
            return s[len(s)-balance : ]  + s[0:len(s)-balance]
        else:             # left
            balance %= -len(s)
            return s[-balance:] + s[:-balance]


def test():
    s = Solution()
    print(s.stringShift("abc", [[1, 1]]))
    print(s.stringShift("abc", [[0, 1]]))
    print(s.stringShift("abcdefg", [[1,1],[1,1],[0,2],[0,3]]))
    print(s.stringShift("mecsk", [[1,4],[0,5],[0,4],[1,1],[1,5]]))


test()