class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        
        @cache
        def dp(i, curr_max, remains):
            if i == len(jobDifficulty):
                if remains == 0:
                    return curr_max
                else:
                    return inf
            
            curr_jd = jobDifficulty[i]
            
            return min(
                curr_max + dp(i+1, curr_jd, remains - 1) ,
                dp(i+1, max(curr_jd, curr_max), remains)
            )
        
        
        return dp(1, jobDifficulty[0], d-1)