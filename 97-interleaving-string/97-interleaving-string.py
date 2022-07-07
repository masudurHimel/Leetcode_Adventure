class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        last = [(0, 0)]
        last = set(last)
        
        if len(s1) + len(s2) != len(s3):
            return False

        for x in s3:
            temp = set()
            for i, j in last:
                if i < len(s1) and s1[i] == x:
                    temp.add((i + 1, j))
                if j < len(s2) and s2[j] == x:
                    temp.add((i, j + 1))

            if not temp:
                return False

            last = temp
        return True
