class WordDictionary:
    # 题意：这题和前缀树模板题的区别是：搜索时，'.'可以匹配任何一个字母
    # 思路：因此，要用DFS进行搜索，碰到'.'时，对所有儿子进行搜索
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = {} # 不要这样写node['#']='#'，这样在搜索时可能会认为它还有孩子

    def search(self, word: str) -> bool: # word碰上终止符，才算搜到。
        def dfs(node, word):
            if not word: # 搜到了完整的字符串，这是终止条件
                if '#' in node:
                    return True
                else:
                    return False
            # 每次都对word[0]进行判断
            if word[0] == '.':
                for c in node: # 遍历node的所有儿子，分别进行dfs
                    # if c == '#':
                    #     continue
                    if dfs(node[c], word[1:]): 
                        return True # 看到True就直接返回，False就继续看下一个儿子
                return False # 遍历完所有儿子都是False，就返回False
            elif word[0] in node:
                c = word[0]
                return dfs(node[c], word[1:])
            else: # 找不到
                return False

        return dfs(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)