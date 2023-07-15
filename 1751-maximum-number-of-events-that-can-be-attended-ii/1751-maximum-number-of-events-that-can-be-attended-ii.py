class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        dp={}
        def helper(pos,prev,k):
            if (pos,prev,k) in dp:
                return dp[(pos,prev,k)]
            if pos==len(events) or k==0:
                return 0
            elif prev>=events[pos][0]:
                dp[(pos,prev,k)]=helper(pos+1,prev,k)
            else:
                l=helper(pos+1,prev,k)
                r=helper(pos+1,events[pos][1],k-1)+events[pos][2]
                dp[(pos,prev,k)]=max(l,r)
            return dp[(pos,prev,k)]
        return helper(0,-1,k)