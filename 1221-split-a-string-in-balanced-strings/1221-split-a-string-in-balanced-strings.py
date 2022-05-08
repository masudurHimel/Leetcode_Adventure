class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res_count = 0
        f_flag = 0
        for i in s:
            if i == 'R':
                f_flag += 1
            if i == 'L':
                f_flag -= 1
            
            if f_flag == 0:
                res_count += 1
            
                
        return res_count