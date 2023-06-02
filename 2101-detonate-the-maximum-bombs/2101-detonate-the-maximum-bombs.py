from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[0 for _ in range(n)] for _ in range(n) ]
        detonate = 0

        def helper(n1, n2):
            x1,y1 = n1[0], n1[1]
            x2 , y2 = n2[0], n2[1]
            r1, r2 = n1[2], n2[2]
            dis12 = sqrt( (x1-x2)**2 + (y1-y2)**2)
            return 1 if r1 >= dis12 else 0
        
        def dfs(node, visited):
            for neighbours in  graph[node]:
                if neighbours not in visited:
                    visited.add(neighbours)
                    dfs(neighbours, visited)
            

        def create_graph(bombs):
            for i in range(n):
                temp = []
                for j in range(n):
                    if i == j: continue
                    if helper(bombs[i], bombs[j]):
                        temp.append(j)
                graph[i] = temp
            return graph

        graph = create_graph(bombs)
        for i in range(n):
            visited = set([i])
            dfs(i, visited)
            detonate = max(detonate, len(visited))
        return detonate