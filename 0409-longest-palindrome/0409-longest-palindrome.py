class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = {}
        res = 0
        max_odd = 0
        
        for i in s:
            seen[i] = seen.get(i, 0) + 1

        for i in seen.values():
            if i%2==0:
                res += i
            else:
                res += i-1 if i>1 else 0
                max_odd = True
        
        if not max_odd:
            return res
        
        return res + 1