class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0
        for i in words:
            temp = set(i)
            if temp <= allowed:
                res += 1
        return res