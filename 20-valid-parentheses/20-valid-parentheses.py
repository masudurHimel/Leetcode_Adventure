class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        res.append(s[0])
        temp_dict = {')': '(', ']': '[', '}': '{'}
        for i in s[1:]:
            if i in [')', '}', ']']:
                if res and temp_dict[i] != res[-1]:
                    return False
                elif res:
                    res.pop()
                else:
                    return False
            else:
                res.append(i)
        if res:
            return False
        else:
            return True