class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        v_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        v = [i for i in s if i in v_set ]
        
        for i, q in enumerate(s):
            if q in v_set:
                s[i] = v.pop()
        return ''.join(s)
                