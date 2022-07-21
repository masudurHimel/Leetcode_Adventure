# class Solution:
#     def maxProfit(self, prices):
#         min_v = 999999999999
#         max_v = 0
#         for i in prices:
#             if i < min_v:
#                 min_v = i
#             if (i - min_v) > max_v:
#                 max_v = i - min_v
#         return max_v

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock_max = deque([])
        max_price = 0
        for i in range(len(prices)-1,-1,-1):
            max_price = max(max_price, prices[i])
            stock_max.appendleft(max_price)
        
        result = -999999
        for i in range(len(prices)):
            result = max(stock_max[i] - prices[i], result)
        
        return result