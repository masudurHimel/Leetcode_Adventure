# from collections import OrderedDict

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = OrderedDict()
        for i in arr:
            res[i] = res.get(i,0) + 1
            
        r = []
        for i, v in res.items():
            if v == 1:
                r.append(i)
                
        if len(r) >= k:
            return r[k-1]
        return ''