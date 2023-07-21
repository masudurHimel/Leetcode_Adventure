class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = []
        pos_seq_len = defaultdict(list)
        
        for num in nums:
            pos = bisect_left(dp, num)
            if pos == len(dp):
                dp.append(num)
            else:
                dp[pos] = num
                
            total = 0
            for count, last in pos_seq_len[pos]:
                if last < num:
                    total += count
                    
            pos_seq_len[pos+1].append((max(1, total), num))
            
        return sum([count for count, _ in pos_seq_len[len(dp)]])