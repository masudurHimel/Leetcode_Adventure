class Solution:
    def extractString(self, target):
        res = []
        for i in range(len(target)):
            if target[i] != '#':
                res.append(target[i])
            elif res:
                res.pop()
        return res
                
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.extractString(s) == self.extractString(t)