class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_counter = 0
        for i in nums:
            if i < 0:
                neg_counter += 1
            elif i == 0:
                return 0
        if neg_counter % 2 != 0:
            return -1
        
        return 1
        