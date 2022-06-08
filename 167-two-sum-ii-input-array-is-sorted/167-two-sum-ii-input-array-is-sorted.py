class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(numbers)):
            if map.get(numbers[i]) == None:
                map[target-numbers[i]] = i
            else:
                return [map[numbers[i]]+1, i+1]
        return [-1,-1]
            