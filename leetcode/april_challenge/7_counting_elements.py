class Solution:
    def countElements(self, arr):
        res = {}
        for i in arr:
            if i not in res:
                res[i] = [1, False]
            else:
                res[i][0] += 1

            if i + 1 in res:
                res[i][1] = True
            if i - 1 in res:
                res[i-1][1] = True

        return sum([val[0] for val in res.values() if val[1]])

    def countElements2(self, arr):
        d = {}
        res = 0
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for i in d:
            if i+1 in d:
                res += d[i+1]

        return res


def test():
    s = Solution()
    for arr in [[1, 2, 3],
                [1, 1, 3, 3, 5, 5, 7, 7],
                [1,3,2,3,5,0],
                [1,1,2,2],
                [1, 1, 2],
                [3,2,1,2,3,0]]:
        print(s.countElements(arr))


test()