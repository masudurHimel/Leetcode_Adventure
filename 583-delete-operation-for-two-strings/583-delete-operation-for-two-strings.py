class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        
        @lru_cache(maxsize=None)
        def solve(p1, p2):
            if len(word1) == p1 or len(word2) == p2:
                return 0

            if word1[p1] == word2[p2]:
                return 1 + solve(p1 + 1, p2 + 1)
            else:
                return max(solve(p1 + 1, p2), solve(p1, p2 + 1))

        res = solve(0, 0)
        
        if res == 0:
            return 2
        
        return abs(res-len(word1)) + abs(res-len(word2))