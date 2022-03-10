class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: [sum((x>>i) & 1 for i in range(32)), x])