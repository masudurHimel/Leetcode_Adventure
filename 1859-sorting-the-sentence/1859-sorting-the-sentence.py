class Solution:
    def sortSentence(self, s: str) -> str:
        t_dict = {}
        s = s.split()
        res = ""
        
        for i in s:
            t_dict[int(i[-1])] = i[:-1]
            
        for i in range(1, len(t_dict)+1):
            res += t_dict[i] + " "
        
        return res[:-1]