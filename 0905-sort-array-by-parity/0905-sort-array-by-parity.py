class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        resEven = []
        resOdd = []
        for i in nums:
            if i%2 == 0:
                resEven.append(i)
            else:
                resOdd.append(i)
        return resEven+resOdd