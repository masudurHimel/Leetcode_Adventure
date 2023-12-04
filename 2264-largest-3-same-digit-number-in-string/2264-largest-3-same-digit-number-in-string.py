class Solution:
    def largestGoodInteger(self, num: str) -> str:
        prev = num[0]
        i = 1
        max_dig = -math.inf
        max_c = 1
        while i < len(num):
            if num[i] != prev:
                prev = num[i]
                max_c = 1
            else:
                max_c += 1
                
            if max_c == 3:
                max_dig = max(max_dig, int(num[i]))
                
            i += 1
                
                
        if max_dig == -math.inf:
            return ""
        return str(max_dig)*3