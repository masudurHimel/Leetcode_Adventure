class Solution:
    def fullBloomFlowers(self, f: List[List[int]], people: List[int]) -> List[int]:
        s,e=sorted([i for i,j in f]),sorted([j for i,j in f])
        return [bisect_right(s,i)-bisect_left(e,i) for i in people]