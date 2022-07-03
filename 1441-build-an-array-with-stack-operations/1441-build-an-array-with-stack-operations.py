class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ind = 0
        res = []
        for i in range(1,n+1):
            if ind >= len(target):
                break
            if i == target[ind]:
                ind += 1
                res.append("Push")
            else:
                res.extend(['Push', 'Pop'])
        return res