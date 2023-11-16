class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])

        def solve(path):
            if(len(path) == n):
                if(path not in nums):
                    return path
                else:
                    return "-1"  

            left = solve(path + '0')
            if(left != "-1"):
                return left
            return solve(path + '1')

        path = ""
        return solve(path)  