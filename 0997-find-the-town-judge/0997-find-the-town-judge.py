class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
            
        d = defaultdict(set)
        t = set()
        for a,b in trust:
            d[b].add(a)
            t.add(a)
        
        # print(d)
        for k, v in d.items():
            if len(v) == n-1 and k not in t:
                return k
        return -1