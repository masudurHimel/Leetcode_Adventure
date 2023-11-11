from queue import PriorityQueue

class Graph:
    graph=[[]]
    def __init__(self, n: int, edges: list[list[int]]):
        self.graph=[[] for i in range(n)]
        for edge in edges:
            self.graph[edge[0]].append((edge[1],edge[2]))

    def addEdge(self, edge: list[int]) -> None:
        self.graph[edge[0]].append((edge[1],edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        pq=PriorityQueue()
        pq.put((0,node1))
        costs=[-1 for i in range(len(self.graph))]
        while(not pq.empty()):
            cost,node=pq.get()
            if(costs[node] != -1):
                continue
            costs[node]=cost
            for child in self.graph[node]:
                if costs[child[0]] == -1:
                    pq.put((child[1]+cost,child[0]))
        return costs[node2]
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)