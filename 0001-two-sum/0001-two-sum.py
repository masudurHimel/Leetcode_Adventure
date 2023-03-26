class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        marker = defaultdict(list)
        for i, v in enumerate(nums):
            marker[v].append(i)
        
        for i in marker:
            f = marker[i].pop()
            if target-i in marker and marker.get(target-i):
                l = marker[target-i].pop()
                return [f, l]
            else:
                marker[i].append(f)
        return [0, 0]