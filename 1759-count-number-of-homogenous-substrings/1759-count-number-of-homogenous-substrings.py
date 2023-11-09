class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        str_list = []
        init_char = s[0]
        init_idx = 0
        c = 0
        for i in range(1, len(s)):
            if s[i] != init_char:
                str_list.append(s[init_idx : i])
                init_char = s[i]
                init_idx = i
        str_list.append(s[init_idx:])

        print(str_list)
        for i in range(len(str_list)):
            len_str = len(str_list[i])
            c += (len_str * (len_str + 1))//2
        
        return c % MOD