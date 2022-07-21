class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_res = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                max_res += prices[i+1] - prices[i]
        return max_res