class Solution:
    def stoneGameIII(self, sv: List[int]) -> str:
        s=0
        dp=[0 for _ in range(50003)]
        for i in range(len(sv)-1,-1,-1):
            dp[i]=-float('inf')
            s+=sv[i]
            for j in range(1,4):
                dp[i]=max(dp[i],s-dp[i+j])
        if s-dp[0]==dp[0]:
            return 'Tie'
        elif s-dp[0]>dp[0]:
            return 'Bob'
        else:
            return 'Alice'