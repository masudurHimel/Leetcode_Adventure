class Solution:
    def findOriginalArray(self, changed):
        if len(changed) % 2 != 0:
            return []

        lm = Counter(changed)
        changed = sorted(changed)
        res = []
        for i in changed:
            if lm.get(i):
                lm[i] = lm[i] - 1
                if lm.get(i * 2):
                    res.append(i)
                    lm[i * 2] = lm[i * 2] - 1
        if len(changed) / 2 == len(res):
            return res
        return []
    