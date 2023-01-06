class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for i in costs:
            if i <= coins:
                res += 1
                coins -= i
            else:
                break
            
            if coins == 0:
                break
        return res
                