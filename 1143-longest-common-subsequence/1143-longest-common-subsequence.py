class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def solve(p1, p2):
            if len(text1) == p1 or len(text2) == p2:
                return 0
            
            if text1[p1] == text2[p2]:
                return 1 + solve(p1+1, p2+1)
            else:
                return max(solve(p1+1,p2), solve(p1, p2+1))
            
        return solve(0,0)