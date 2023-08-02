class Solution:
    def compress(self, chars):
        res = []
        chars.append("|")
        prev = chars[0]
        counter = 1
        for i in chars[1:]:
            if i == prev:
                counter += 1
            elif i != prev:
                res.append(prev)
                if counter > 1:
                    res.append(str(counter))
                counter = 1

            prev = i
        res = ''.join(res)
        for i in range(len(res)):
            chars[i] = res[i]
        return len(res)