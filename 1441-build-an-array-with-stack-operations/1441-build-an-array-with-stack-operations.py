class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ind = 1
        res = []
        for i in target:
            if i == ind:
                ind += 1
                res.append("Push")
            elif diff := i - ind:
                res.append("Push")
                while diff > 0:
                    res.append("Pop")
                    res.append("Push")
                    ind += 1
                    diff -= 1
                ind += 1
        
        return res