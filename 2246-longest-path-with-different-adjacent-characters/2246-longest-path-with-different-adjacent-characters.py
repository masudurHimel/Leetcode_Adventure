class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        adjacentList = [[] for _ in range (n)]
        
        for i in range(1, n):
            adjacentList[i].append(parent[i])
            adjacentList[parent[i]].append(i)
        ans = 1
        def dfs(cur, prev):
            nonlocal ans
            if len(adjacentList[cur]) == 1 and cur != 0:
                return 1
            first, second = 0, 0
            for nei in adjacentList[cur]:
                if nei == prev: 
                    continue 
                temp = dfs(nei, cur)
                if s[cur] != s[nei]:
                    if temp > first:
                        second = first 
                        first = temp 
                    elif temp > second:
                        second = temp 
            if ans < 1 + first + second: ans = 1 + first + second 
            return 1 + first 
        dfs(0, -1)
        return ans 