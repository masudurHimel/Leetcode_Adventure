class Solution:
    def partitionString(self, s):
        visited = set()
        i = 0
        res = []
        t = ""
        while i < len(s):
            if s[i] in visited:
                visited = {s[i]}
                res.append(t)
                t = s[i]
            else:
                t += s[i]
                visited.add(s[i])
            i += 1

        if t:
            res.append(t)
        return len(res)