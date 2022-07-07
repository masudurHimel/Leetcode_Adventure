class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = []
        for i in logs:
            if i == '../' and len(res) >= 1:
                res.pop()
            elif i == '../':
                pass
            elif i == './':
                pass
            else:
                res.append(i[:-1])
        print(res)
        
        return len(res)