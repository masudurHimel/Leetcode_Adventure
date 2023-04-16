class Solution:
    MOD = 10**9+7

    def numWays(self, words: List[str], target: str) -> int:
        word_len = len(words[0])
        histograms: MutableSequence[MutableMapping[str, int]] = [
            defaultdict(int) for _ in range(word_len)
        ]
            
        for word in words:
            for i, c in enumerate(word):
                histograms[i][c] += 1
        
        previous_dp = [1] * (word_len+1)
        for target_idx, c in enumerate(target):
            dp = [0] * (word_len+1)
            remaining = len(target) - target_idx
    
            for hist_idx in range(target_idx, word_len-remaining+1):
                c_freq = histograms[hist_idx][c]
                dp[hist_idx+1] = ((c_freq * previous_dp[hist_idx]) + dp[hist_idx]) % self.MOD

            previous_dp = dp

        return dp[-1]