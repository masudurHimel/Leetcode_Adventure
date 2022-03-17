class Solution:
    def singleNumber(self, nums: List[int]):
        res_dict = {}
        
        for i in nums:
            res_dict[i] = res_dict.get(i, 0) + 1
        
        for k, v in res_dict.items():
            if v == 1:
                return k
            
        