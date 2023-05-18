class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph_tracker = [0] * n
        for edge in edges:
            graph_tracker[edge[1]] += 1
        res = []
        
        for i in range(n):
            if graph_tracker[i] == 0:
                res.append(i)
                
        return res