class Solution:
    def romanToInt(self, s: str) -> int:
        res_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'Q': 4,
                   'W': 9, 'E': 40, 'R': 90, 'T':400, 'Y': 900}
        finder_dict = {'IV': 'Q', 'IX': 'W', 'XL': 'E', 'XC': 'R', 'CD': 'T', 'CM': 'Y'}
        for i in range(len(s)-1):
            _ = s[i:i+2]
            if s[i:i+2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                s = s[:i] + finder_dict[_] + s[i+2:]
        res = 0
        for i in enumerate(s):
            res += res_dict[i[1]]
        return res