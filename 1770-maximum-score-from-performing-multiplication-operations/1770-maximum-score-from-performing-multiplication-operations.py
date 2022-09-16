class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        s=0
        n=len(nums)
        m=len(multipliers)

        res=[[0]*(m+1) for i in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(i, -1, -1):
                f=nums[j]*multipliers[i]+res[i+1][j+1]
                l=nums[n-1-(i-j)]*multipliers[i]+res[i+1][j]
                res[i][j]=max(f, l)
        return res[0][0]