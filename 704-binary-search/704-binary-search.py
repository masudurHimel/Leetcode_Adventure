class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) -1
        while l<=h:
            mid = (l+h)//2
            print(mid, l, h)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else:
                h = mid-1
        return -1