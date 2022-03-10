class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i in range(1, len(arr)+1, 2):
            for j in range(len(arr)):
                if j+i <= len(arr):
                    res += sum(arr[j:j+i])
        return res