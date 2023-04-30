class UnionFind:
    def __init__(self, n):
        self.par = {i: i for i in range(1, n + 1)}
        self.rank = {i: 1 for i in range(1, n + 1)}
    
    def find(self, n1):
        while n1 != self.par[n1]:
            self.par[n1] = self.par[self.par[n1]]
            n1 = self.par[n1]
        return n1
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return 1
        if self.rank[p1] < self.rank[p2]:
            p1, p2 = p2, p1
        self.par[p2] = p1
        self.rank[p1] += self.rank[p2]
        return 0
    

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        
        res = 0
        for t, i, j in edges:
            if t == 3 and (alice.union(i, j) or bob.union(i, j)):
                res += 1
        
        for t, i, j in edges:
            if t == 1 and alice.union(i, j):
                res += 1
            if t == 2 and bob.union(i, j):
                res += 1
        
        a = sum(1 for i in range(1, n + 1) if alice.find(i) == i)
        b = sum(1 for i in range(1, n + 1) if bob.find(i) == i)
        
        return res if a == b == 1 else -1