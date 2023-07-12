class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outdegree = defaultdict(int)
        nodes_coming_in = defaultdict(list)
        zero_outdegree = []
        ans = []
        for i, nodes in enumerate(graph):
            outdegree[i] = len(nodes)
            if outdegree[i] == 0:
                zero_outdegree.append(i)
            for node in nodes:
                nodes_coming_in[node].append(i)

        while zero_outdegree:
            node = zero_outdegree.pop()
            for nd in nodes_coming_in[node]:
                outdegree[nd] -= 1
                if outdegree[nd] == 0:
                    zero_outdegree.append(nd)
            ans.append(node)
        ans.sort()         
        return ans