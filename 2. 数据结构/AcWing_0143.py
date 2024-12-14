class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 2

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, x: int) -> None:
        node = self.root
        for i in range(31, -1, -1):
            bit = (x >> i) & 1
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def query(self, x: int) -> int:
        node = self.root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (x >> i) & 1
            toggled_bit = 1 - bit
            if node.children[toggled_bit]:
                max_xor |= (1 << i)
                node = node.children[toggled_bit]
            else:
                node = node.children[bit]
        return max_xor


if __name__ == '__main__':
    trie = Trie()
    n = int(input())
    nums = list(map(int, input().split()))
    for num in nums:
        trie.insert(num)

    ans = 0
    for num in nums:
        ans = max(ans, trie.query(num))

    print(ans)
