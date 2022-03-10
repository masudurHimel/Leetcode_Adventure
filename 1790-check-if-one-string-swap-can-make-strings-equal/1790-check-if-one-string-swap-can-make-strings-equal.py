class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if sorted(list(s1)) != sorted(list(s2)):
            return False
        if s1 == s2:
            return True
        
        diff_list = []
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_list.append(s1[i])
        
        return len(diff_list) == 2