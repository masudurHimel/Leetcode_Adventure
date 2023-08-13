class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[n] = True
        
        for i in range(n-2, -1, -1):
            if i == n-2:
                dp[i] = nums[i] == nums[i + 1]
                continue
                
            
            dp[i] = nums[i] == nums[i+1] and dp[i+2]
            if dp[i]: continue
            
            dp[i] = nums[i] == nums[i+1] == nums[i+2] and dp[i+3]
            if dp[i]: continue
                
            dp[i] = nums[i] + 1 == nums[i+1] and nums[i+1] + 1 == nums[i+2] and dp[i+3]
        
        return dp[0]