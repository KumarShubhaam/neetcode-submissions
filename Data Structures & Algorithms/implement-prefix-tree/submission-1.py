class TrieNode: 
    def __init__(self):
        self.children = {}
        self.ends = False

class PrefixTree:

    def __init__(self):
        self.start = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.start
        for c in word:
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]
        temp.ends = True
        return

    def search(self, word: str) -> bool:
        temp = self.start
        for c in word:
            if c not in temp.children:
                return False
            temp = temp.children[c]
        return temp.ends        

    def startsWith(self, prefix: str) -> bool:
        temp = self.start
        for c in prefix:
            if c not in temp.children:
                return False
            temp = temp.children[c]
        return True
        
        