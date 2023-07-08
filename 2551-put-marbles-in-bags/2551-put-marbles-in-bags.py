class Solution:
    def putMarbles(self, w: List[int], k: int) -> int:
        if k==1:return 0
        p=[0]*(len(w)-1)
        for i in range(len(w)-1):
           p[i]=w[i]+w[i+1]
        p.sort()
        print(p)
        return sum(p[-k+1:])-sum(p[:k-1]) 