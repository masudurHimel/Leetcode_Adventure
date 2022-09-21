class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        prev_sum = 0
        for j in nums:
            if j % 2 == 0:
                prev_sum += j
        
        print(prev_sum)

        for t in queries:
            v, i = t[0], t[1]
            
            if nums[i]%2!=0 and (nums[i]+v) % 2 == 0:
                nums[i] += v
                prev_sum += nums[i]
                
                
            elif nums[i]%2!=0 and (nums[i]+v) % 2 != 0:
                nums[i] += v
            
            elif nums[i]%2==0 and (nums[i]+v) % 2 != 0:
                prev_sum -= nums[i]
                nums[i] += v
            
            elif nums[i]%2==0 and (nums[i]+v) % 2 == 0:
                prev_sum -= nums[i]
                nums[i] += v
                prev_sum += nums[i]
            
            res.append(prev_sum)
            
        return res