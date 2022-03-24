class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote, magazine = list(ransomNote), list(magazine)
        
        for i in ransomNote:
            if i in magazine:
                magazine.remove(i)
            else:
                return False
        return True