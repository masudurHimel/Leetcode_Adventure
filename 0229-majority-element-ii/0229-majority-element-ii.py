class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        threshold = len(nums)//3 
        res = []
        for k, v in counter.items():
            if v > threshold:
                res.append(k)
        return res