class Solution:
    @staticmethod
    def totalBalanceCheck(x):
        sum_list = 0
        for i in x:
            sum_list += i
        return sum_list

    def maximumWealth(self, accounts):
        res = []
        for i in accounts:
            res.append(self.totalBalanceCheck(i))
        res.sort()
        return res[-1]