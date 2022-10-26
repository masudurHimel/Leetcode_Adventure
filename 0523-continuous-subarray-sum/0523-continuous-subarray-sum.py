class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sums = defaultdict(lambda:float(inf))
        running_sum = 0
        
        for i, n in enumerate(nums):
            running_sum += n
            mod_sum = running_sum%k
            
            if i >= 1 and (mod_sum == 0 or prefix_sums[mod_sum] < i - 1):
                return True
            prefix_sums[mod_sum] = min(prefix_sums[mod_sum], i)
                
        return False