import heapq

class Solution:
    def lastStoneWeight(self, stones):
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)
            heapq.heappush(stones, (-(a - b)))

        return -stones[0]


def test():
    s = Solution()
    print(s.lastStoneWeight([2,7,4,1,8,1]))
    print(s.lastStoneWeight([1, 3]))
    print(s.lastStoneWeight([3, 7, 8]))
    print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))

test()
