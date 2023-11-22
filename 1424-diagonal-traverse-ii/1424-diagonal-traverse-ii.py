class Solution(object):
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        map_ = defaultdict(list)
        for i in range(len(nums) - 1 , -1, -1):
            for j in range(len(nums[i]) - 1, -1, -1):
                map_[i+j].append(nums[i][j])
        output = []
        for i in range(len(map_)):
            output.extend(map_[i])
        return output