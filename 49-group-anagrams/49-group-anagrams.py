class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            _ = str(sorted(i))
            res[_] = res.get(_, []) + [i]
        return res.values()
            
            
            