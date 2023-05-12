class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = [0] * (len(questions))
        def dp(i):
            if i >= len(questions):
                return 0
            if cache[i]:
                return cache[i]
            cache[i] = max(dp(i + 1), questions[i][0] + dp(i + 1 + questions[i][1]))
            return cache[i]
        return dp(0)