class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = 0
        for i in num:
            res = res * 10 + i
        res += k
        return list(str(res))