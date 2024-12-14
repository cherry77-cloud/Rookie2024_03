class UnionFind:
    def __init__(self, size: int) -> None:
        self.fa = list(range(size))

    def get(self, x: int) -> int:
        root = x
        while self.fa[root] != root:
            root = self.fa[root]
        while self.fa[x] != root:
            self.fa[x], x = root, self.fa[x]
        return root

    def merge(self, a: int, b: int) -> None:
        self.fa[self.get(a)] = self.get(b)


if __name__ == "__main__":
    n, m = map(int, input().split())
    uf = UnionFind(n + 1)

    for _ in range(m):
        parts = input().split()
        op = parts[0]
        a = int(parts[1])
        b = int(parts[2])

        if op == 'M':
            uf.merge(a, b)
        elif op == 'Q':
            if uf.get(a) == uf.get(b):
                print("Yes")
            else:
                print("No")
