class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        val = prices[0]
        profit = 0

        for i in prices:
            if i < val:
                val = i
            elif i > val:
                profit += (i - val)
                val = i

        return profit