class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        res = "".join(words)
        hashmap = {}
        for i in res:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        n = len(words)
        for i in hashmap.values():
            if i%n != 0:
                return False
        return True