class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        target_val = 0
        for i in digits:
            target_val = target_val * 10 + i
        target_val = list(str(target_val+1))
        return target_val
        