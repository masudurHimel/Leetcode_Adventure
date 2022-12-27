class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        for i in range(len(capacity)):
            capacity[i] -= rocks[i]
        capacity = sorted(capacity)
        
        cnt = 0
        
        for i in range(len(capacity)):
            if additionalRocks == 0:
                break
            
            if capacity[i] != 0:
                if capacity[i] <= additionalRocks:
                    additionalRocks -= capacity[i]
                    capacity[i] = 0
            
            
        return capacity.count(0)