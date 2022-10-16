class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        arr.sort(reverse=True)
        for i in arr:
            if i == c.get(i):
                return i
        return -1