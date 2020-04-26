class Solution:
    def checkValidString(self, s):
        lo, hi = 0, 0

        for c in s:
            if c == "(":
                lo += 1
                hi += 1
            elif c == ")":
                lo -= 1
                hi -= 1
            else:
                lo -= 1
                hi += 1
            if hi < 0:
                return False
            lo = max(lo, 0)

        return lo == 0

    def checkValidString2(self, s):

        def check(stack, s):
            while s:
                c = s.pop(0)
                print(c)
                if c == "(":
                    stack.append(c)
                elif c == ")":
                    if not stack:
                        return False
                    else:
                        stack.pop()
                else:
                    return (check(stack[:] + ["("], s[:]) or
                            check(stack[:], s[:]) or
                            (stack and check(stack[:-1], s[:])))

            return stack == []

        return check([], list(s))


def test():
    s = Solution()
    for test_str in [
                    #"()", "(*)", "(*))", "((*)", "()()",
                    #"((*",
                    #"((*)"
                    #"(*)(*)))",
                    "*()(",
                    #"((())()()(*)(*()(())())())()()((()())((()))(*"
                    ]:
        print("=== {} ===".format(test_str))
        print(s.checkValidString(test_str))


test()
