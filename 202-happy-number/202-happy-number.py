class Solution:
    @staticmethod
    def getNextNumber(n):
        total_sum = 0
        while n > 0:
            _ = n%10
            n = n//10
            total_sum += _ ** 2
        return total_sum
            
    def isHappy(self, n: int) -> bool:
        res_track = [n]
        while True:
            n = self.getNextNumber(n)
            if n == 1:
                return True
            elif n in res_track:
                return False
            else:
                res_track.append(n)
                
            