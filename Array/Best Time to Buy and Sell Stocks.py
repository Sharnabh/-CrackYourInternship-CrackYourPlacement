class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = float('inf'), float('-inf')

        for i in prices:
            minPrice = min(i, minPrice)
            maxProfit = max(maxProfit, (i - minPrice))

        return maxProfit