class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap_counter = 0
        for i in word:
            if 'A' <= i <='Z':
                cap_counter += 1
                
        if cap_counter == 0:
            return True
        
        if (cap_counter > 0) and ('A'<=word[0]<='Z'):
            pass
        else:
            return False
        
        if cap_counter == 1 or cap_counter == len(word):
            return True
        return False