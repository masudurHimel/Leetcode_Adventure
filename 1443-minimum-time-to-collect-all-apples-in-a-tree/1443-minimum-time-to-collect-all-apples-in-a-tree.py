class Solution(object):
    def minTime(self, n, edges, hasApple):
        adj = defaultdict(set)
        self.ans = 0
        visited = set()
        
        if not sum(hasApple):
            return 0

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        def dfs(curr):
            visited.add(curr)
            has_apple = hasApple[curr]
            for child in adj[curr]:
                if child not in visited:
                    temp = dfs(child)
                    self.ans += 1
                    if not temp:
                        self.ans -= 2
                    self.ans += 1
                    has_apple |= temp
            return has_apple

        dfs(0)
        return self.ans