class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = defaultdict(list)
        for i in arr:
            res[abs(x-i)].append(i)
        
        ans = []
        for i in sorted(res):
            ans += res[i]
            if len(ans) > k:
                break
        return sorted(ans[:k])