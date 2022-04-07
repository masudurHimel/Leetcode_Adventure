class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        print(stones)
        while True:
            if len(stones) >= 2:
                if stones[-2] == stones[-1]:
                    stones = stones[:-2]
                else:
                    stones = stones[:-2] + [stones[-1]-stones[-2]]
                    
            if len(stones) <= 1:
                break
            stones = sorted(stones)

        
        if len(stones) == 0:
            return 0
        
        return stones[0]