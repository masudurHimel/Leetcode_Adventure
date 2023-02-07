class Solution:
    def totalFruit(self, fruits):
        count = dict()
        i = 0
        for j in range(len(fruits)):
            count[fruits[j]] = count.get(fruits[j], 0) + 1
            if len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
        return j - i + 1