class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        max_move = 10 * n
        move = 0
        res = []
        
        def check(x):
            for i in range(m):
                if x[i] == stamp[i] or x[i] == '?':
                    continue
                return False
            return True
        
        while move < max_move:
            temp = move
            for i in range(n-m+1):
                if check(target[i:i+m]):
                    move += 1
                    res.append(i)
                    target = target[:i] + '?' * m + target[i+m:]

                    if target == '?'*n:
                        return res[::-1]
            if move == temp:
                return []