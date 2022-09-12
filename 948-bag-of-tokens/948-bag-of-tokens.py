class Solution:
    def bagOfTokensScore(self, tokens, power):
        st = sorted(tokens)
        score = 0
        max_score = 0
        i = 0
        j = len(st) - 1
        while power > 0 or score > 0:
            if i > j:
                break

            if st[i] <= power:
                power -= st[i]
                i += 1
                score += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += st[j]
                j -= 1
                score -= 1
            else:
                break
        return max_score