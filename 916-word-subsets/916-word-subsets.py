class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = set()
        neg = set()
        
        temp_words_1 = []
        temp_words_2 = {}
        
        for i in words1:
            temp_words_1.append(Counter(i))
        
        for i in words2:
            for j in i:
                c = i.count(j)
                if j not in temp_words_2 or c > temp_words_2.get(j):
                    temp_words_2[j] = c
        
        
        for i in temp_words_2.keys():
            for j in range(len(words1)):
                if temp_words_2[i] <= temp_words_1[j].get(i, 0):
                    res.add(words1[j])
                else:
                    neg.add(words1[j])
        return res-neg
        # print(neg)
            