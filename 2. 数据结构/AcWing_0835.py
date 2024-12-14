class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.count = 0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.count += 1

    def query(self, word: str) -> int:
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return 0
            node = node.children[index]
        return node.count


if __name__ == '__main__':
    trie = Trie()
    n = int(input())
    for _ in range(n):
        op, word = input().split()
        if op == 'I':
            trie.insert(word)
        else:
            print(trie.query(word))
