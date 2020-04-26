

class Solution:
    def groupAnagrams(self, strs):
        res = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss not in res:
                res[ss] = [s]
            else:
                res[ss].append(s)

        return list(res.values())

def test():
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

test()