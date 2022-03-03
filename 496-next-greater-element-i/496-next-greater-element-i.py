class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = []
        for i in nums1:
            flag = 0
            _ = nums2.index(i)
            for j in nums2[_ + 1:]:
                if j > i:
                    res.append(j)
                    flag = 1
                    break

            if flag == 0:
                res.append(-1)
        return res