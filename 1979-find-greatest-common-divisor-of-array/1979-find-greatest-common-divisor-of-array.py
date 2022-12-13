class Solution:
    
    @staticmethod
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return abs(x)
    
    def findGCD(self, nums: List[int]) -> int:
        return self.gcd(min(nums), max(nums))