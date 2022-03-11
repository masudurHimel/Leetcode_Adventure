class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) -1
        flag = -1
        while l<=h:
            mid = (l+h)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid+1
                flag = mid
            else:
                h = mid-1
            
        return l