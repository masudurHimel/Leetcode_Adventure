class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res = ""
        for i in s:
            if i == " ":
                k -= 1
            if k == 0:
                break
            res += i
        return res