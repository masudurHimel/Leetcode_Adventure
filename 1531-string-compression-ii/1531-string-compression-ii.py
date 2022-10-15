class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        N=len(s)
        if N==k:
            return 0
        
        @lru_cache(None)
        def memo(last,count,index,left):
            if index==N:
                return 0
            best=math.inf
            if last!=-1 and s[index]==last:
                score=0
                if count<=1 or count+1==10 or count+1==100:
                    score=1
                    
                best=min(best,memo(last,count+1,index+1,left)+score)
                if left>=1:
                    best=min(best,memo(last,count,index+1,left-1))
                    
            else:
                best=min(best,memo(s[index],1,index+1,left)+1)
                if left>=1:
                    best=min(best,memo(last,count,index+1,left-1))
                    
            return best
        
        return memo(-1,0,0,k)