class Solution:
    def addToArrayForm(self, num: List[int], k: int):
        res = 0
        for i in num:
            res = res * 10 + i
        res += k
        r = []
        for i in list(str(res)):
            r.append(int(i))
        return r