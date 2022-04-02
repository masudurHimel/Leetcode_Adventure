class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        p = len(s)-1
        for i in range(len(s)):
            if s[i]!=s[p]:
                tmpA = s[:i]+s[i+1:]
                tmpB = s[:p]+s[p+1:]
                if tmpA == tmpA[::-1] or tmpB==tmpB[::-1]:
                    return True
                break
            p = p-1 
        return False
            