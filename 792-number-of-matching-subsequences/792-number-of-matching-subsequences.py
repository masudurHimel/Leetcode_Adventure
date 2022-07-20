class Solution:
    def numMatchingSubseq(self, s: str, words) -> int:
        
        def isSubSet(s, word):
            word = list(word)

            for i in range(len(s) - 1, -1, -1):
                if not word:
                    break
                if s[i] == word[-1]:
                    word.pop()

            return word == []
        
        res = 0
        res_map = {}
        s = list(s)
        for word in words:
            key = word
            if word not in res_map:
                if isSubSet(s, word):
                    res_map[word] = True
                    res+=1
                else:
                    res_map[word] = False
            else:
                if res_map[word]:
                    res += 1

        return res