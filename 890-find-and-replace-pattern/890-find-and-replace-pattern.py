class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            if len(set(word)) == len(set(pattern)):
                temp_map = {}
                status = True
                for i in range(len(pattern)):
                    if pattern[i] not in temp_map:
                        temp_map[pattern[i]] = word[i]
                    elif temp_map.get(pattern[i], -1) != word[i]:
                        status = False
                        break
                if status:
                    res.append(word)
        return res