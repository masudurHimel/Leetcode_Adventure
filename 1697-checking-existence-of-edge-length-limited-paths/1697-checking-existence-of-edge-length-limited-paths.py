class DisjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size = [1]*(n+1)

    def unionBySize(self,u,v):
        ulp_u = self.findParent(u)
        ulp_v = self.findParent(v)

        if ulp_u == ulp_v: return

        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

    
    def findParent(self,n):
        if n == self.parent[n]:
            return n
        self.parent[n] = self.findParent(self.parent[n])
        return self.parent[n]


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])
        queries = sorted([(p,q,limit,i) for i,(p,q,limit) in enumerate(queries)],key=lambda x: x[2])

        ds = DisjointSet(n)
        res = [False]*len(queries)
        cur_edge = 0

        for p,q,limit,i in queries:
            while cur_edge < len(edgeList) and edgeList[cur_edge][2] < limit:
                u,v,dist = edgeList[cur_edge]
                ds.unionBySize(u,v)
                cur_edge += 1

            if ds.findParent(p) == ds.findParent(q):
                res[i] = True

        return res