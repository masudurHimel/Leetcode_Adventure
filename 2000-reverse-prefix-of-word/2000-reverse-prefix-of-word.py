class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            return word[word.index(ch)::-1] + word[word.index(ch)+1:]
        except Exception as e:
            return word