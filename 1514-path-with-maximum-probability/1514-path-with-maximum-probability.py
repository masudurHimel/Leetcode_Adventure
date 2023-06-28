class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        graph = defaultdict(list)

        for (i,j),p in zip(edges,succProb):
            graph[i].append((j,-math.log(p)))
            graph[j].append((i,-math.log(p)))

        dict1 = {i:float("inf") for i in range(n)}

        dict1[start], stack = 0, [(0,start)]

        while stack:
            weight, node = heappop(stack)

            for neighbor,w in graph[node]:
                if dict1[neighbor] > weight + w:
                    dict1[neighbor] = weight + w
                    heappush(stack,(weight+w,neighbor))

        return math.pow(math.e,-dict1[end])