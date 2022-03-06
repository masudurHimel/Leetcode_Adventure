class Solution:
    def mergeAlternately(self, word1: str, word2: str):
        min_len = min(len(word1), len(word2))
        res = ''
        for i in range(min_len):
            res += word1[i] + word2[i]
        
        i +=1 
        
        if i < len(word1):
            res += word1[i:]
        elif i < len(word2):
            res += word2[i:]
        return res
            
            