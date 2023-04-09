class Solution:
    def largestPathValue(self, coloring: str, edges: List[List[int]]) -> int:
        N = len(coloring)
        degree = [0] * N
        node_color = {node:color for node, color in enumerate(coloring)}
        adj = collections.defaultdict(set)
        for n_1, n_2 in edges:
            adj[n_1].add(n_2)
            degree[n_2] +=1
        
        bfs = [n for n, deg in enumerate(degree) if deg == 0]
        colors = {n:{letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"} for n in range(N)}
        result = 0
        for n in bfs:
            colors[n][node_color[n]] += 1
            result = max(result, colors[n][node_color[n]])
            for nb in adj[n]:
                degree[nb] -= 1
                for c in "abcdefghijklmnopqrstuvwxyz":
                    colors[nb][c] = max(colors[nb][c], colors[n][c])
                if degree[nb] == 0:
                    bfs.append(nb)
        return result if len(bfs) == N else -1