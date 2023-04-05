class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = Counter(ransomNote)
        mn = Counter(magazine)
        
        for k, v in rn.items():
            t = mn.get(k, 0)
            if t < v:
                return False
        return True
            