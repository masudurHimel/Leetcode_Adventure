class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            target = nums1
            sec_target = nums2
        else:
            target = nums2
            sec_target = nums1
            
        res = []
        
        for i in target:
            if i in sec_target:
                sec_target.remove(i)
                res.append(i)
        return res