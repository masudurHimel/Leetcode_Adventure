class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_res = {}
        rev_res = {}
        res = []
        for i in nums:
            count_res[i] = count_res.get(i,0)+1
            
        print(count_res)
        
        for i in count_res.keys():
            rev_res[count_res[i]] = rev_res.get(count_res[i], []) + [i]
            
        print(rev_res)

        res = []
        for i in range(len(nums),-1,-1):
            if rev_res.get(i) is not None:
                res.extend(rev_res[i]) 
            if len(res) >= k:
                return res
        return res
            
        
        