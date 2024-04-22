class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        v = [i for i in s if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] ]
        
        for i, q in enumerate(s):
            if q in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                s[i] = v.pop()
        return ''.join(s)
                