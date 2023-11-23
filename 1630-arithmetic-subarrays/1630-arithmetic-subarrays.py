class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def query_checker(arr):
            min_item = min(arr)
            max_item = max(arr)
          
            diff = (max_item - min_item) / (len(arr) - 1)
            if diff % 1:
                return False
            
            uniques = set(arr)
            curr = min_item
            while curr < max_item:
                if curr not in uniques:
                    return False
                curr += diff
            return True

        res = []
        for i in range(len(r)):
            res.append(query_checker(nums[l[i]: r[i] + 1]))
        return res