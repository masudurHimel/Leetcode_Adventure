class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = []
        for i in s:
            if i.lower() in ['a','e', 'i', 'o', 'u']:
                 vowels.append(i)
        f = len(vowels) - 1
        for i, v in enumerate(s):
            if v.lower() in ['a','e', 'i', 'o', 'u']:
                s[i] = vowels[f]
                f -= 1
        
        return ''.join(s)
        
                 