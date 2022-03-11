class Solution:
    def isPalindrome(self, s: str) -> bool:
        res_str = ''
        for i in s:
            i = i.lower()
            if (i>='a' and i<='z') or (i>='0' and i<='9') :
                res_str += i
        
        return res_str == res_str[::-1]
        