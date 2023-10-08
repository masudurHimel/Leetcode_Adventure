class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        min_value = -1000 * 1000
        n, m = len(nums1), len(nums2)


        dp = [[min_value]*(m+1) for _ in range (n+1)]
        pre_max = [[min_value]*(m+1) for _ in range (n+1)]

        max_prod = min_value

        for i in range(n+1):
            dp[i][0] = 0
            pre_max[i][0] = 0
        
        for i in range(m+1):
            dp[0][i] = 0
            pre_max[0][i] = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = pre_max[i-1][j-1] + nums1[i-1]*nums2[j-1]
                max_prod = max(max_prod, dp[i][j])
                pre_max[i][j] = max(pre_max[i-1][j], pre_max[i][j-1], dp[i][j])
        
        return max_prod