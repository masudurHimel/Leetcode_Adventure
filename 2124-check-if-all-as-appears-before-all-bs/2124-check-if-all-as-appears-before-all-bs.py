class Solution:
    def checkString(self, s: str) -> bool:
        flag = False
        
        for i in s:
            if i == 'b':
                flag = True
            if flag and i == 'a':
                return False
        return True