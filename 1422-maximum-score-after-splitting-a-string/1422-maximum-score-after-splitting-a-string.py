class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)

        suffix_count = 1 if s[-1] == '1' else 0
        suffix_counts = [-1] * n
        suffix_counts[n - 1] = suffix_count

        for i in range(1, n):
            if s[n - 1 - i] == '1':
                suffix_count += 1
            suffix_counts[n - 1 - i] = suffix_count

        prefix_count = 1 if s[0] == '0' else 0
        max_score = prefix_count + suffix_counts[1]

        for i in range(1, n - 1):
            if s[i] == '0':
                prefix_count += 1
            max_score = max(max_score, prefix_count + suffix_counts[i + 1])

        return max_score
