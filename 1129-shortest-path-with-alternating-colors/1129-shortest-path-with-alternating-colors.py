class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(n)}
        for x,y in redEdges:
            graph[x].append([y,"R"])
        
        for x,y in blueEdges:
            graph[x].append([y,"B"])
        
        def bfs(node):
            queue = collections.deque([[0,-1,0]])
            visited = set()
            visited.add((0,-1))
            while len(queue)>0:
                
                curr_node,prev_color,curr_dist = queue.popleft()
                if curr_node == node:
                    return curr_dist
                for children,color in graph[curr_node]:
                    if prev_color == -1:
                        if (children,color) not in visited:
                            queue.append([children,color,curr_dist+1])
                            visited.add((children,color))
                    elif prev_color == "R":
                        if color == "B":
                            if (children,color) not in visited:
                                queue.append([children,color,curr_dist+1])
                                visited.add((children,color))
                    elif prev_color == "B":
                        if color == "R":
                            if (children,color) not in visited:
                                queue.append([children,color,curr_dist+1])
                                visited.add((children,color))
            
            return -1
            
            
        ans = [0]
        for i in range(1,n):
            dist = bfs(i)
            ans.append(dist)
        
        return ans