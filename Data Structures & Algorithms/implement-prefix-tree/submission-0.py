class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur_root = self.root
        for c in word:
            if c not in cur_root:
                cur_root[c] = {}
            cur_root = cur_root[c]
        cur_root['#'] = {}

    def search(self, word: str) -> bool:
        cur_root = self.root
        for c in word:
            if c not in cur_root:
                return False
            cur_root = cur_root[c]
        if '#' not in cur_root:
            return False
        else:
            return True

    def startsWith(self, prefix: str) -> bool:
        cur_root = self.root
        for c in prefix:
            if c not in cur_root:
                return False
            cur_root = cur_root[c]
        return True
        
        