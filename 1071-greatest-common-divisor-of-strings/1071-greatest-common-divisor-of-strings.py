class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        
        # if l1 % 2 == 0 and l2 % 2 != 0:
        #     return ""
        # if l1 % 2 != 0 and l2 % 2 == 0:
        #     return ""
        
        c = math.gcd(l1, l2)
        res = str1[:c]
        # print(c, res)
        
        return res if res*(l1//c) == str1 and res*(l2//c) == str2 else ""