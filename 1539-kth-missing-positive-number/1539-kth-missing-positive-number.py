class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res = [i for i in range(1, arr[-1]+k+1)]
        res = list(set(res)^set(arr))
        res = sorted(res)
        return res[k-1]