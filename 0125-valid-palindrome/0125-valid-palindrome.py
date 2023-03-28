class Solution:
    def isPalindrome(self, s: str) -> bool:
        f, l = 0, len(s) - 1
        s = s.lower()
        while f < l:
            flag = 0
            # print(s[f], s[l])
            if not (('a' <= s[f] <= 'z') or ('0' <= s[f] <= '9')):
                f += 1
                flag = 1
            if not (('a' <= s[l] <= 'z') or ('0' <= s[l] <= '9')):
                l -= 1
                flag = 1

            if flag:
                continue

            if s[f] != s[l]:
                print(s[f], s[l])
                return False
            f += 1
            l -= 1

        return True