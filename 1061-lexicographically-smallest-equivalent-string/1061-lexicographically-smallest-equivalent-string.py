class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        hashmap = defaultdict(list)

        for i in range(len(s1)):
            hashmap[s1[i]].append(s2[i])
            hashmap[s2[i]].append(s1[i])

        self.visited = set()
        self.res = defaultdict(list)
        temp = []

        def dfs(node):
            if node not in self.visited:
                self.visited.add(node)
                temp.append(node)
                for i in hashmap[node]:
                    dfs(i)

        for key in hashmap:
            dfs(key)
            temp.sort()

            for i in temp:
                self.res[i] += temp
            temp = []

        res = ""
        
        for i in baseStr:
            if len(self.res[i]) != 0:
                res += self.res[i][0]
            else:
                res += i

        return res
