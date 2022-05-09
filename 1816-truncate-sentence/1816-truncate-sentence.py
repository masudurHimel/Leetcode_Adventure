class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        res = ""
        for i in s[:k]:
            res += i + " "
            
        return res[:-1]