class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        left = 0
        cur = ans = 0
        for right in range(len(s)):
            if s[right] in vowels:
                cur += 1
            if right - left >= k:
                if s[left] in vowels:
                    cur -= 1
                left += 1
            ans = max(ans, cur)
        return ans