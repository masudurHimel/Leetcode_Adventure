class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        temp = set(words1)
        letters = {}
        for i in words2:
            for j in i:
                c = i.count(j)
                if j not in letters or c > letters.get(j):
                    letters[j] = c
        
        for i in range(len(words1)):
            for j in letters.keys():
                if words1[i].count(j) < letters[j]:
                    temp.remove(words1[i])
                    break
        return list(temp)