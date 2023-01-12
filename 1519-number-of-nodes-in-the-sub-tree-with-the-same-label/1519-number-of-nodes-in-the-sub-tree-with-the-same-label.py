class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] * n
        tree = collections.defaultdict(list)
        for a, b in edges:                             
            tree[a].append(b)
            tree[b].append(a)
        def dfs(node):                                 
            nonlocal visited, ans, tree
            c = Counter(labels[node])
            for i in tree[node]:
                if i in visited: continue           
                visited.add(i)
                c += dfs(i)                          
            ans[node] = c.get(labels[node])            
            return c
        visited = set([0])
        dfs(0)
        return ans