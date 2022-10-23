class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        visited = set()
        for i in nums:
            if i in visited:
                repeat = i
            else:
                visited.add(i)
        
        start, end = min(visited), max(visited)
        
        if start != 1:
            return [repeat, 1]
        if end != len(nums):
            return [repeat, end+1]
        
        for i in range(start, end):
            if i not in visited:
                return [repeat, i]
        return []
                