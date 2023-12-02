class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        col = Counter(chars)
        res = 0
        for word in words:
            s = Counter(word)
            flag = 0
            for k, v in s.items():
                if k in col and v <= col[k]:
                    pass
                else:
                    flag = 1
                    break
            if flag == 0:
                res += len(word)
                    
        
        return res