class Solution:
    def myAtoi(self, s: str) -> int:
        sc = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-'}
        scu = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        
        res = ""
        for i in s:
            if i == ' ' and res == '':
                continue
            if i in sc:
                if res == '':
                    sc = scu
                res += i
            else:
                break

        if not res:
            return 0
        
        if len(res) <= 1 and res[0] in {'+', '-'}:
            return 0
        
        if (-2**31) < int(res) < (2**31-1):
            return int(res)
        
        return -2**31 if res[0] == '-' else 2**31-1