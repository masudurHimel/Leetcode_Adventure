class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        temp = set(words1)
        letters = {}
        for i in words2:
            temp_dict = {}
            for j in i:
                temp_dict[j] = temp_dict.get(j, 0) + 1
            
            for j in temp_dict:
                if j not in letters or temp_dict[j] > letters.get(j):
                    letters[j] = temp_dict[j]
        
        for i in range(len(words1)):
            for j in letters.keys():
                if words1[i].count(j) < letters[j]:
                    temp.remove(words1[i])
                    break
        return list(temp)