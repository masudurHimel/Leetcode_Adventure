class Solution:
    def removeStars(self, s):
        res = []
        
        for i in s:
            if i != '*':
                res.append(i)
            else:
                res.pop()
        return "".join(res)
        