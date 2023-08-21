class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2):
            res_str = s[:]
            if len(res_str.replace(res_str[:i+1], '')) == 0:
                return True
        return False