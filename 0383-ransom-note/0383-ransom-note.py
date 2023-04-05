class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = Counter(ransomNote)
        mn = Counter(magazine)
        
        for k, v in rn.items():
            if t := mn.get(k):
                if t < v:
                    return False
            else:
                return False
        return True
            