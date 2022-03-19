class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        res = []
        for i in arr:
            if i == 0:
                res += [0,0]
            else:
                res.append(i)
        arr[:] = res[:len(arr)]
        