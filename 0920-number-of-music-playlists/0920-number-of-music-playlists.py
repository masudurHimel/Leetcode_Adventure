class Solution:
    @cache
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        
        if n<=k: return 0
        res = 1
        for i in range(n-k+1,n+1): res *= i
        res *= (n-k)**(goal-k)
        for i in range(k,n): res -= self.numMusicPlaylists(i,goal,k) * comb(n,i)
        
        return res % (10**9+7)