class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        substring_len = len(words) * len(words[0])
        word_map = Counter(words)
        
        def helper(i):
            word_counter = word_map.copy()
            word_used = 0
            
            for j in range(i, i+substring_len, len(words[0])):
                target = s[j:j+len(words[0])]
                if word_counter[target] > 0:
                    word_counter[target] -= 1
                    word_used += 1
                # else:
                #     break
            return word_used == len(words)
        
        res = []
        for i in range(len(s)-substring_len+1):
            if helper(i):
                res.append(i)
        return res
            