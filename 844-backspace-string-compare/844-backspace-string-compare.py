class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # return True
        x = []
        y = []
        
        for i in range(len(s)):
            if s[i] != '#':
                x.append(s[i])
            else:
                if x:
                    x.pop()
                
        for i in range(len(t)):
            if t[i] != '#':
                y.append(t[i])
            else:
                if y:
                    y.pop()
        

        print(x,y)
        return x == y