class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = {}
        
        for i in range(len(nums)):
            if nums[i] in res and abs(i-res.get(nums[i])) <=k:
                return True
            else:
                res[nums[i]] = i
        return False