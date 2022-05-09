class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, k = [], 0
        for i in s:
            if i ==')':
                k -= 1
            if k > 0:
                res.append(i)
            if i == '(':
                k += 1
            
        return "".join(res)