class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        if source == destination:
            return True
        paths = defaultdict(set)
        for a, b in edges:
            paths[a].add(b)
            paths[b].add(a)

        p = deque([source])
        valid_path = set()

        while p:
            n = p.popleft()
            if n == destination:
                return True

            for i in paths[n]:
                if i not in valid_path:
                    valid_path.add(i)
                    p.append(i)
        return False