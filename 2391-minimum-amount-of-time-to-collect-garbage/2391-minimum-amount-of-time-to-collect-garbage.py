class Solution:
    def garbageCollection(self, g: List[str], t: List[int]) -> int:
        lm, lg, lp, tm, tp, tg = -1, -1, -1, 0, 0, 0
        tl = len(g) - 1

        for i in range(len(g) - 1, -1, -1):
            if 'G' in g[i] and lg <= -1:
                lg, tg = i, sum(t[:i])
            if 'P' in g[i] and lp <= -1:
                lp, tp = i, sum(t[:i])
            if 'M' in g[i] and lm <= -1:
                lm, tm = i, sum(t[:i])

        lenn = len(''.join(g))
        return lenn + tp + tg + tm