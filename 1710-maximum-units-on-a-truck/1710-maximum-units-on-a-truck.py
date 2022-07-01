class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x:x[1], reverse=True)
        res = 0
        for i in boxTypes:
            unit = min(i[0], truckSize)
            res += (unit*i[1])
            truckSize -= unit
            if truckSize < 0:
                break
        return res