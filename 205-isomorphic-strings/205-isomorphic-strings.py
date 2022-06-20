class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        
        for k, i in enumerate(s):
            s_hash[i] = s_hash.get(i, []) + [k]
        
        for k, i in enumerate(t):
            t_hash[i] = t_hash.get(i, []) + [k]
        
        for i in zip(s_hash.values(), t_hash.values()):
            if i[0]!=i[1]:
                return False
        return True