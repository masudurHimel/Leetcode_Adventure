class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        x = []
        res = 0
        for i in range(len(strs[0])):
            t = []
            for j in range(len(strs)):
                t.append(strs[j][i])
            
            if t == sorted(t):
                x.append(t)
            else:
                res += 1
        return res