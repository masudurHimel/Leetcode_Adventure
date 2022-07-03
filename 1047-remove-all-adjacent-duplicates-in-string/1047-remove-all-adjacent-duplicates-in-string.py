class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 0
        n = len(s) - 1
        while i < n:
            print(i)
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                i = max(0, i-1)
            else:
                i += 1
            n = len(s) - 1
        return s