class Solution:
    def myAtoi(self, s: str) -> int:
        sc = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-'}
        res = ""
        for i in s:
            if i == ' ' and res == '':
                continue
            if i in sc:
                if res == '':
                    sc.remove('+')
                    sc.remove('-')
                res += i
            else:
                break
        
        # print(res)
        # return 0
        
        if not res:
            return 0
        
        if len(res) <= 1 and res[0] in {'+', '-'}:
            return 0
        
        if len(res) > 1 and res[1] in {'+', '-'}:
            return 0
        
        if (-2**31) < int(res) < (2**31-1):
            return int(res)
        
        if res[0] == '-':
            return -2**31
        else:
            return 2**31 -1