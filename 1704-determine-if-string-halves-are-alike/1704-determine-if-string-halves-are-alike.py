class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        targetA, targetB = s[:len(s)//2], s[len(s)//2:]
        temp_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        res = 0
        
        for i in targetA:
            if i in temp_list:
                res += 1
        
        for i in targetB:
            if i in temp_list:
                res -= 1
        
        
        return res == 0
        