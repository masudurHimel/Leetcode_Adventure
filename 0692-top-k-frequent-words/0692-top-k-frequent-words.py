class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        res = defaultdict(list)
        for i, v in c.items():
            res[v].append(i)
           
        a = []
        for i in sorted(res.keys(), reverse=True):
            if k <= 0:
                break
                
            v = res[i]
            
            if len(v) > 1:
                a += sorted(v)[:k]
            else:
                a += v
            
            k -= len(v)
        
        return a