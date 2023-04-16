class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pChecker = 0
        nChecker = 0
        for i in nums:
            if i >= 0:
                if (pChecker & 1<<i)>0:
                    return True
                pChecker |= (1 << i)

            if i<0:
                i = abs(i)
                if(nChecker & 1<<i)>0:
                    return True
                nChecker |= (1<<i)
        return False