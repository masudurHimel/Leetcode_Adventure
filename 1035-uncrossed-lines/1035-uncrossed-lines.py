class Solution:
    n1 = []
    n2 = []
    
    @cache
    def dfs(self, i, sub, res):
        if i >= len(self.n1):
            return res

        source = self.n1[i]
        newRes = 0
        newSub = 0
        if source in self.n2[sub:]:
            target = self.n2[sub:].index(source)
            newRes = res + 1
            newSub = sub + target + 1
        i += 1

        path1 = 0
        if newRes and newSub:
            path1 = self.dfs(i, newSub, newRes)
        path2 = self.dfs(i, sub, res)

        return max(path1, path2)

    def maxUncrossedLines(self, nums1, nums2):
        self.n1 = nums1
        self.n2 = nums2
        
        return self.dfs(0, 0, 0)