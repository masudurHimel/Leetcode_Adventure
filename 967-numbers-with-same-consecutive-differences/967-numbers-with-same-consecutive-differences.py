class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        queue = deque((1,i) for i in range(1,10))
        
        while queue:
            i, v = queue.pop()
            if i == n:
                res.append(v)
            else:
                for j in range(10):
                    if abs(v%10 - j) == k:
                        queue.append((i+1, (v*10)+j))
        return res