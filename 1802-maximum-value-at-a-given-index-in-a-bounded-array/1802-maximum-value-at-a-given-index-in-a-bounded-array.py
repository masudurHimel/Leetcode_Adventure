class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        if n==1:
            return maxSum
        def cal(v,i):
            ans=0
            # leftside cal
            if v>i:
                s=(i*(2*(v-1)+(i-1)*(-1)))/2
                ans+=s
            else:
                nn=(v-1)
                s=(nn*(2*(v-1)+(nn-1)*(-1)))//2
                ss=(i-nn)
                ans+=s
                ans+=ss
            
            # rightside cal
            r=n-i-1
            if v>r:
                ans+=((r*(2*(v-1)+(r-1)*(-1)))/2)
            else:
                nn=(v-1)
                s=(nn*(2*(v-1)+(nn-1)*(-1)))//2
                ss=(r-nn)
                ans+=s
                ans+=ss
            return ans+v
        
        l=0;h=maxSum
        while l<h:
            m=(l+h)//2
            if cal(m,index)<=maxSum:
                l=m+1
            else:
                h=m
        return l-1