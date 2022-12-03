class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        counter = sorted(counter.items(), key=lambda x:x[1], reverse=True)
        res = ''
        for i in counter:
            res += i[0] * i[1]
        return res