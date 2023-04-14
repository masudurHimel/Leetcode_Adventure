class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        m=[[1 for x in range(n)] for y in range(n)]
        for ss in range(1,n):
            for i in range(n-ss):
                j=i+ss
                if s[i]==s[j] and ss==1:
                    m[i][j]=2

                elif s[i]==s[j]:
                    m[i][j]=m[i+1][j-1]+2

                else:
                    m[i][j]=max(m[i+1][j],m[i][j-1])


        return m[0][-1]                    