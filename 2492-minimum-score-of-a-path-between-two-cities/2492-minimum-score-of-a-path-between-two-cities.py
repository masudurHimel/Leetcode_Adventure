class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for a, b, d in roads:
            graph[a][b] = d
            graph[b][a] = d
        print(graph)
        min_score = math.inf
        visited = set()
        queue = deque([1])

        while queue:
            node = queue.popleft()
            for nd, dist in graph[node].items():
                if nd not in visited:
                    queue.append(nd)
                    visited.add(nd)
                min_score = min(min_score, dist)
        return min_score