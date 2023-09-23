class Solution(object):
    def longestStrChain(self, words):
        n = len(words)
        d= []
        for word in words:
            temp = []
            for i in range(len(word)):
                temp.append(word[:i]+word[i+1:])
            d.append( (len(word), word, set(temp)))

        d = sorted(d)
        dp = [1]*n 
        for i in range(n):
            for j in range(i+1, n):
                if d[j][0] > d[i][0]+1:
                    break
                if d[i][1] in d[j][2]:
                    dp[j] = max(dp[j], dp[i]+1)

        return max(dp)