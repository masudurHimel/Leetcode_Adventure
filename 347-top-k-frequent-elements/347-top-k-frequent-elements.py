class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_res = {}
        res = []
        for i in nums:
            count_res[i] = count_res.get(i,0)+1
        count_res = {k: v for k, v in sorted(count_res.items(), key=lambda item: item[1], reverse=True)} 
        return list(count_res.keys())[:k]
        