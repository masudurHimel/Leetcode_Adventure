class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sorted_nums  = sorted(nums)
        # print(sorted_nums)
        sum_pair_nums = []
        l,r = 0, len(sorted_nums) -1
        while l<r:
            sum_pair_nums.append(sorted_nums[l] + sorted_nums[r])
            l +=1
            r -=1

        return max(sum_pair_nums)