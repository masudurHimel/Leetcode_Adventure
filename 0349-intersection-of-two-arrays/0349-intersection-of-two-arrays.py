class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        res = []
        for i in nums1:
            if nums2.get(i):
                res.append(i)
        return res