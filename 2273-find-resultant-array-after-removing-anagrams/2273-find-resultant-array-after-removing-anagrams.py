class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        def isAnagram(s, t):
            if len(s) != len(t):
                return False
            s = Counter(s)
            t = Counter(t)
            

            for i in s.keys():
                if t.get(i,0) != s[i]:
                    return False
            return True
        
        i = 1
        while i < len(words):
            status = isAnagram(words[i], words[i-1])
            if status:
                words.pop(i)
            else:
                i += 1
        
        return words