class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        last_digit = -1
        for i in s.split():
            if i.isdigit():
                if int(i) > last_digit:
                    last_digit = int(i)
                else:
                    return False
        return True