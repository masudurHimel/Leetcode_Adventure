class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(node):
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
        
        N = len(isConnected)
        
        graph = defaultdict(list)
        for r in range(N-1):
            for c in range(r+1, N):
                if isConnected[r][c]:
                    graph[r].append(c)
                    graph[c].append(r)
            
        visited = [False]*N
        count = 0
        for node in range(N):
            if not visited[node]:
                count += 1
                dfs(node)
        
        return count