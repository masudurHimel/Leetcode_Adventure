class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letter_dict = dict()
        lx = 65
        for i in range(1, 27):
            letter_dict[i] = chr(lx)
            lx += 1
        res = ""

        while columnNumber > 0:
            temp = columnNumber % 26
            if temp == 0:
                temp = 26
            res = letter_dict[temp] + res
            columnNumber = int((columnNumber - temp) / 26)
        return res