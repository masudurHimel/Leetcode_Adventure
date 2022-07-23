class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        f_res = []
        sorted_nums = sorted(nums)
        for ind, i in enumerate(nums):
            temp_ind = bisect_left(sorted_nums, i)
            f_res.append(temp_ind)
            del sorted_nums[temp_ind]
        
        return f_res