class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)-1
        res = list()
        
        def dfs(node, path=[]):
            path = path + [node]
            if node == n: 
                res.append(path)
                return
            for v in graph[node]:
                dfs(v, path)

        dfs(0)
        return res