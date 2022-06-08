class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        min_flag = True
        source = [] + nums
        target = []
        
        while n > 1:
            for i in range(0,n,2):
                if min_flag:
                    target.append(min(source[i], source[i+1]))
                    min_flag = False
                else:
                    target.append(max(source[i], source[i+1]))
                    min_flag = True
            
            n = len(target)
            source = target
            target = []
        
        return source[0]