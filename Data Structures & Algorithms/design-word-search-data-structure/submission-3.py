class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = False

class WordDictionary:
    def __init__(self):
        self.start = TrieNode()        

    def addWord(self, word: str) -> None:
        temp = self.start
        for c in word:
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]
        temp.ends = True
        return

    def searchHelper(self, word: str, temp: TrieNode) -> bool:
        # print('search:', word)
        if len(word) == 0:
            return temp.ends

        word_length = len(word)
        for i in range(word_length):
            c = word[i]
            if c != '.':
                if c not in temp.children:
                    return False
                temp = temp.children[c]
            else:
                for curr in temp.children.values():
                    subAns = self.searchHelper(word[i+1:], curr)
                    if subAns:
                        return True
                return False                    
                            
        return temp.ends     

    def search(self, word: str) -> bool:
        temp = self.start
        return self.searchHelper(word, temp)
        

