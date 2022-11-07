class Solution:
    def maximum69Number (self, num: int) -> int:
        org = num
        num = list(str(num))
        for i in range(len(num)):
            if num[i] != '9':
                num[i] = '9'
                return ''.join(num)
        return org