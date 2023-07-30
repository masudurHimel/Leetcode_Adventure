class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        
        for i in range(max(len(word1), len(word2))):
            if i < len(word1) and i < len(word2):
                res += word1[i] + word2[i]
            elif i < len(word1):
                res += word1[i]
            elif i < len(word2):
                res += word2[i]
            
        return res