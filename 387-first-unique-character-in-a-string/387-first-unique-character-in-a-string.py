class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0
        
        visited = []
        for i in range(len(s)):
            if s[i] not in visited  and s[i+1:].count(s[i]) == 0:
                return i
            else:
                visited.append(s[i])
        return -1