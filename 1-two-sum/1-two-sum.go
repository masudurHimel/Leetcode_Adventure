class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if map.get(nums[i]) == None:
                map[target-nums[i]] = i
            else:
                return [map[nums[i]], i]
        return [-1,-1]