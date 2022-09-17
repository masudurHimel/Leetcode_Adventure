class Solution:

    def palindromePairs(self, words):
        res = []
        c = {}
        for i, v in enumerate(words):
            c[v[::-1]] = i

        for i in range(len(words)):
            for j in range(len(words[i])+1):
                pre, post = words[i][:j], words[i][j:]

                if not len(pre) == 0 and pre == pre[::-1] and post in c and c[post] != i:
                    res.append([c[post], i])

                if post == post[::-1] and pre in c and c[pre] != i:
                    res.append([i, c[pre]])

        return res
