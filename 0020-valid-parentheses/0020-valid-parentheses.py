class Solution:
    def isValid(self, s: str) -> bool:
        ref = {"(": ")", "{": "}", "[":"]"}
        stack = []
        for i in s:
            if i in ref:
                stack.append(i)
            elif not stack:
                return False
            else:
                temp = stack.pop()
                if ref[temp] != i:
                    return False
        if stack:
            return False
        return True
                    
            
        