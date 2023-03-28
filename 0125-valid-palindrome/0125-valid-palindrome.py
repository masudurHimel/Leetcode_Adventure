class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [i for i in s if (i>='a' and i<='z') or (i >='0' and i<='9')]
        return s == s[::-1]