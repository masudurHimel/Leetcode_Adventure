class Solution:
    def minimumRounds(self, tasks) -> int:
        tasks = Counter(tasks)
        if 1 in tasks.values():
            return -1
        res = 0
        for n in tasks.values():
            res += n // 3 + bool(n % 3)
        return res