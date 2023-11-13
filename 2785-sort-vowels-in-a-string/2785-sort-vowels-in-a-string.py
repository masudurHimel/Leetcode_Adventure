class Solution:
    def sortVowels(self, s: str) -> str:
        v_list = []
        res = []
        
        v_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        v_l = []
        
        for i in s:
            if i in v_set:
                res.append('a')
                v_l.append(i)
            else:
                res.append(i)
        
        if not v_l:
            return s
        
        v_l.sort()
        r = ""
        target = 0
        for v in res:
            if v == 'a':
                v = v_l[target]
                target += 1
            r += v
        
        return r
                