class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        note = {} 
        res = 0
        for i in arr:
            if not i-difference in note: 
                note[i] = 1
            else:
                note[i] = note[i-difference] + 1 
            res = max(res, note[i])

        return res