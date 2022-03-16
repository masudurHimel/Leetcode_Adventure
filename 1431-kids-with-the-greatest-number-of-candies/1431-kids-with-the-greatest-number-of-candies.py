class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_can = max(candies)
        res = []
        for i in candies:
            _ = i + extraCandies
            if _ >= max_can:
                res.append(True)
            else:
                res.append(False)
        return res