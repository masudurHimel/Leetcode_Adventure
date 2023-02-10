class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        helper = {')': '(', ']': '[', '}': '{'}
        res = [s[0]]
        for i in s[1:]:
            if target := helper.get(i):
                if res and target == res[-1]:
                    res.pop()
                else:
                    return False
            else:
                res.append(i)
        return False if res else True