class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for i in strs:
            _ = sorted(list(i))
            if x := res.get(str(_)):
                x = x + [i]
                res[str(_)] = x
            else:
                res[str(_)] = [i]
        
        f_res = []
        for v in res.values():
            f_res.append(v)
        
        return f_res
            
            
            