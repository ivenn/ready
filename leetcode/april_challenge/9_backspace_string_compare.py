class Solution:
    def backspaceCompare(self, S, T):

        def build_stack(s):
            res = []
            for c in s:
                if c.isalpha():
                    res.append(c)
                elif res:
                    res.pop()
            return res

        return build_stack(S) == build_stack(T)

    def backspaceCompare2(self, S, T):
        skipS, skipT = 0, 0
        i, j = len(S) - 1, len(T) - 1

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0 and S[i] != T[j]:
                return False
            if (i >= 0) != (j >= 0):
                return False
            i -= 1
            j -= 1

        return True

def test():
    s = Solution()
    print(s.backspaceCompare2("y#fo##f", "y#f#o##f"))


test()
