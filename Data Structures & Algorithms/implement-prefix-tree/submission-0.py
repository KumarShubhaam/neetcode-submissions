class PrefixTree:

    def __init__(self):
        self.d = {}        

    def insert(self, word: str) -> None:
        temp = self.d
        for c in word:
            temp[c] = temp.get(c, {'ends': False})
            temp = temp[c]
        temp['ends'] = True
        # print(self.d)
        return

    def search(self, word: str) -> bool:
        temp = self.d
        for c in word:
            if c not in temp.keys():
                return False
            temp = temp[c]
        if temp['ends']:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        temp = self.d
        for c in prefix:
            if c not in temp.keys():
                return False
            temp = temp[c]
        return True
        
        