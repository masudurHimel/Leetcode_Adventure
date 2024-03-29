class Solution:
    def reorganizeString(self, S: str) -> str:
        counter = collections.Counter(S)
        i, res, n = 0, [None] * len(S), len(S)
        for k in sorted(counter, key = counter.get, reverse = True):
            if counter[k] > n // 2 + (n % 2): return ""
            for j in range(counter[k]):
                if i >= n: i = 1
                res[i] = k; i += 2
        return "".join(res)