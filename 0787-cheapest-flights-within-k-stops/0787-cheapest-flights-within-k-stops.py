class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        distances = [float('inf')] * n
        distances[src] = 0
        for i in range(K+1):
            temp = distances.copy()
            for u, v, w in flights:
                temp[v] = min(temp[v], distances[u] + w)
            distances = temp
        return -1 if distances[dst] == float('inf') else distances[dst]

        