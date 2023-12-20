class Solution(object):
    def buyChoco(self, prices, money):
        prices.sort()
        remaining_money = money - prices[0] - prices[1]

        if remaining_money >= 0:
            return remaining_money
        else:
            return money