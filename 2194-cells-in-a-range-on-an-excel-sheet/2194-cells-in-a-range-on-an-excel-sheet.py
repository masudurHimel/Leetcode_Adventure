class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []
        f, l = s.split(':')
        
        if f[-1] == l[-1]:
            res = [chr(i)+f[-1] for i in range(ord(f[0]), ord(l[0])+1)]
        
        else:
            for i in range(ord(f[0]), ord(l[0])+1):
                for j in range(int(f[-1]), int(l[-1])+1):
                    res.append(chr(i)+str(j))
                    
        
        return res