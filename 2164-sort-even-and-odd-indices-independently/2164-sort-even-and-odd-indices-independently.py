class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        l1, l2 = list(), list()
        
        for i in range(len(nums)):
            if i % 2 != 0:
                l2.append(nums[i])
            else:
                l1.append(nums[i])
        
        l1 = sorted(l1)
        l2 = sorted(l2, reverse=True)
        
        res = []
        while l1 and l2:
            res.append(l1.pop(0))
            res.append(l2.pop(0))
        
        if l1:
            res += l1
        elif l2:
            res += l2
            
        return res