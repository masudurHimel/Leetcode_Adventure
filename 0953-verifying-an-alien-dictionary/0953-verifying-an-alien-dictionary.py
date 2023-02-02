class Solution:
    def isAlienSorted(self, words: List[str], order: str):
        return words == sorted(words, key=lambda word: [order.index(letter) for letter in word ]) 