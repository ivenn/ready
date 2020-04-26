class Solution:
    def maxProfit(self, prices):
        res = [0] * len(prices)
        for x in range(len(prices)):
            for y in range(x, len(prices)):
                res[y] = max(res[y-1], res[x] + (prices[y] - prices[x]))

        return res[-1]

    def maxProfit2(self, prices):
        res = 0

        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i-1])

        return res


def test():
    s = Solution()
    print(s.maxProfit2([7,1,5,3,6,4]))
    print(s.maxProfit2([1,2,3,4,5]))
    print(s.maxProfit2(list(range(10000,1,-1))))


test()

