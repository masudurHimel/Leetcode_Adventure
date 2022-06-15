class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        f,l = 0, len(s)-1
        s = list(s)
        
        while f < l:
            if s[f].isalpha() and s[l].isalpha():
                s[f], s[l] = s[l], s[f]
                f += 1
                l -= 1
            elif not s[f].isalpha():
                f += 1
            else:
                l -= 1
            
        return ''.join(s)