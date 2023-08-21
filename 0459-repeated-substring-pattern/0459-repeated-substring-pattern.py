class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2):
            res_str = s[:]
            # print(res_str)
            _ = res_str.replace(res_str[:i+1], '')
            # print(_)
            # print(len(_))
            if len(_) == 0:
                return True
        return False