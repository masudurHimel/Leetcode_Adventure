class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        tl = []
        res = 0
        colors += 'x'
        for i in range(len(colors)-1):
            if colors[i] == colors[i+1]:
                tl.append(neededTime[i])
            elif colors[i] != colors[i+1] and tl:
                tl.append(neededTime[i])
                tl.sort()
                print(tl)
                res += sum(tl[:len(tl)-1])                
                tl = []
        return res