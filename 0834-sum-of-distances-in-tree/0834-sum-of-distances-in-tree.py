class Solution:
    def sumOfDistancesInTree(self, n: int, edges):
        graph = defaultdict(set)
        res = [0] * n
        count = [1] * n

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        def dfs(root, pre):
            for i in graph[root]:
                if i != pre:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]

        def dfs2(root, pre):
            for i in graph[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + n - count[i]
                    dfs2(i, root)

        dfs(0, -1)
        dfs2(0, -1)
        return res