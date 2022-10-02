class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def helper(mem, n, target):
            if target <= 0 or target > (n*k):
                return 0
            if n == 1:
                return 1
            if (n, target) in mem:
                return mem[(n, target)]
            
            res = 0
            for i in range(1, k+1):
                res += helper(mem, n-1, target -i)
            mem[(n, target)] = res
            return mem[(n,target)]
        
        return helper(dict(), n, target) % (10**9 + 7)