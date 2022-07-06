class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = [num//3-1, num//3, num//3+1]
        return x if sum(x) == num else []
       