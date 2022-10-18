class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        
        res = []
        s = nums[0]
        e = nums[0]
        
        for ind, i in enumerate(nums[1:]):
            if i == e + 1:
                e = i
            else:
                if s == e:
                    res.append(str(s))
                else:
                    res.append(f"{s}->{e}")
                s = i
                e = i
        if s != e:
            res.append(f"{s}->{e}")
        else:
            res.append(str(s))
        return res