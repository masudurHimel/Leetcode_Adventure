class Solution:
    def fillCups(self, amount) -> int:
        res = 0
        while amount[0] > 0 or amount[1] > 0 or amount[2] > 0:
            amount = sorted(amount, reverse=True)
            res += 1
            amount[0] -= 1
            amount[1] -= 1
        return res