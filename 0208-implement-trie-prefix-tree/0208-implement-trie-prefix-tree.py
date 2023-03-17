class Trie:

    def __init__(self):
        self.words = set()
        

    def insert(self, word: str) -> None:
        self.words.add(word)
        

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        for i in self.words:
            if i.startswith(prefix):
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)