class Solution:
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
        
    
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res