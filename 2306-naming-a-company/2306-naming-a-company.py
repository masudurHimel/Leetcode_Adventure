class Solution:
    def distinctNames(self, ideas):
        mp = defaultdict(set)
        for idea in ideas:
            mp[idea[0]].add(idea[1:])

        count = 0
        Keys = list(mp.keys())
        nkey = len(Keys)
        Sizes = [0] * nkey

        for i in range(nkey):
            Sizes[i] = len(mp[Keys[i]])

        for i in range(1, nkey):
            for j in range(i):
                sizeA, sizeB = Sizes[i], Sizes[j]
                keyA, keyB = Keys[i], Keys[j]
                sizeI = len(mp[keyA].intersection(mp[keyB]))
                count += (sizeA - sizeI) * (sizeB - sizeI)
        return count * 2