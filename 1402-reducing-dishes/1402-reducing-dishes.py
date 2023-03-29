class Solution:
    def maxSatisfaction(self, sa: List[int]) -> int:
        sa = sorted(sa)
        n = len(sa)

        lastSum = 0
        curSum = 0
        i=n-1
        while(i>=0 and sa[i] > 0):
            curSum += sa[i]
            lastSum += curSum
            i-=1
        if(i==-1 or lastSum == 0):
            return lastSum

        best = lastSum

        while(i>=0):   
            curSum += sa[i]
            lastSum += curSum
            best = max(best,lastSum)
            i-=1
        return best