class Solution:
    def makesquare(self, nums):
        if not nums:
            return False

        possible_side =  sum(nums) // 4

        if possible_side * 4 != sum(nums):
            return False

        nums.sort(reverse=True)

        sums = [0] * 4

        def dfs(index):

            if index == len(nums):
                return sums[0] == sums[1] == sums[2] == possible_side

            for i in range(4):
                if sums[i] + nums[index] <= possible_side:
                    sums[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    sums[i] -= nums[index]
            return False        
        return dfs(0)