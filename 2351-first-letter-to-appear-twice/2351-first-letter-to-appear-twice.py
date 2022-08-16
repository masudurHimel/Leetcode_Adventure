class Solution:
    def repeatedCharacter(self, s: str) -> str:
        res_map = {}
        
        for i in s:
            if res_map.get(i):
                return i
            res_map[i] = True
        return None