class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nc = Counter(nums)
        for k, v in nc.items():
            if v >= math.ceil(len(nums)/2):
                return k
        return 0