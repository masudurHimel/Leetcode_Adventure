class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range (1,len(nums)):
            nums[i]+=nums[i-1]
        sol=[]
        for i in queries:
            t=0
            for x in nums:
                if x>i:
                    break
                t+=1
            sol.append(t)
        return sol