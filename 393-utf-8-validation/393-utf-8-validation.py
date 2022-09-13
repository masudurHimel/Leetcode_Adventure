class Solution:
    def validUtf8(self, data) -> bool:
        if len(data) == 1:
            temp = bin(data[0])[2:]
            if len(temp) < 8:
                temp = '0' * (8-len(temp)) + temp
                if temp.find('0') != 0:            
                    return False

        temp_count = 0
        for i in data:
            i = bin(i)[2:]
            if len(i) < 8:
                i = '0' * (8-len(i)) + i
                
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