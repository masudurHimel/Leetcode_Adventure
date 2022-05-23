class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for i in strs:
            _ = sorted(i)
            _ = str(_)
            if x := res.get(_):
                x = x + [i]
                res[_] = x
            else:
                res[_] = [i]
        
        f_res = []
        for v in res.values():
            f_res.append(v)
        
        return f_res
            
            
            