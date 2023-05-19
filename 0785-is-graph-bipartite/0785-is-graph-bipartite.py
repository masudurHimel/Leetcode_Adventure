class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [2 for _ in range(n)]
        
        def recurse(index):
            if count == n:
                return True
        
            current_color = colors[index]
            
            for nei in graph[index]:
                if colors[nei] == 2:
                    colors[nei] = current_color ^ 1
                    if not recurse(nei):
                        return False
                elif colors[nei] == current_color:
                    return False
                
            return True
        
        for index in range(n):
            if colors[index] == 2:
                colors[index] = 0
                if not recurse(index):
                    return False
        
        return True  