class Solution:
    def validUtf8(self, data) -> bool:
        for i in range(len(data)):
            data[i] = bin(data[i])[2:]
            if len(data[i]) < 8:
                data[i] = '0' * (8-len(data[i])) + data[i]

        if len(data) == 1 and data[0].find('0') != 0:
            return False

        temp_count = 0
        for i in data:
            if temp_count > 0:
                if i[:2] != '10':
                    return False
                temp_count -= 1
                if temp_count == 1:
                    temp_count -= 1
                continue

            if temp_count == 0:
                temp_count = i.find('0')
                if temp_count > 4:
                    return False
                if temp_count == -1:
                    temp_count = 8

        if temp_count >= 1:
            return False
        return True