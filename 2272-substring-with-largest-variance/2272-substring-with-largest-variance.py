import string

class Solution:
    def largestVariance(self, s: str) -> int:

        def l_variance(s, up, down):
            running_sum = 0
            current_min_to_use = float('inf')
            soon_to_be_min = 0
            result = 0

            for c in s:
                if c == up:
                    running_sum += 1
                    result = max(result, running_sum - current_min_to_use)
                elif c == down:
                    current_min_to_use = min(current_min_to_use, soon_to_be_min)
                    running_sum -= 1
                    result = max(result, running_sum - current_min_to_use)   
                    soon_to_be_min = min(soon_to_be_min, running_sum)

            return result 

        
        result = 0
        for c_up in string.ascii_lowercase:
            for c_down in string.ascii_lowercase:
                if c_up == c_down:
                    continue 
                result = max(result, l_variance(s, c_up, c_down))

        return result