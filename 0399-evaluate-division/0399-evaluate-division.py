class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1. / v))
        
        def query(src, dst):
            dists = {src: 1}
            q = collections.deque([(1, src)])
            while q:
                dist, u = q.popleft()
                for v, weight in graph[u]:
                    if v in dists:
                        continue
                    if v == dst and dst in dists:  # check for more than one path to dst
                        return -1.0
                    dists[v] = dist * weight
                    q.append((dists[v], v))

            return dists[dst] if dst in dists else -1.0
        
        output = []
        for src, dst in queries:
            # find a single path between c and d in the graph, return the product of weights
            # if there is no path, or there is more than one path, return -1.0
            q = query(src, dst) if src in graph else -1.0
            output.append(q)
        
        return output