class WordDictionaryNode:
    __slots__ = ('children', 'is_end')
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = WordDictionaryNode()

    def addWord(self, word):
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = WordDictionaryNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word):
        stack = [(self.root, 0)]
        while stack:
            node, i = stack.pop()
            if i == len(word):
                if node.is_end:
                    return True
                continue
            ch = word[i]
            if ch == '.':
                for child in node.children:
                    if child:
                        stack.append((child, i + 1))
            else:
                idx = ord(ch) - ord('a')
                if node.children[idx]:
                    stack.append((node.children[idx], i + 1))
        return False