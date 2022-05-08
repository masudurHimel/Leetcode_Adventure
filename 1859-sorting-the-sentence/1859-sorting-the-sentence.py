class Solution:
    def sortSentence(self, s: str) -> str:
        s_sen = {}
        s = s.split()
        res = ""
        
        for i in s:
            s_sen[int(i[-1])] = i[:-1]
            
        for i in range(1, len(s_sen)+1):
            res += s_sen[i] + " "
        
        return res[:-1]