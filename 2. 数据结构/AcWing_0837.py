class UnionFind:
    def __init__(self, size) -> None:
        self.fa = list(range(size))
        self.cnt = [1] * size

    def get(self, x: int) -> int:
        if self.fa[x] != x:
            self.fa[x] = self.get(self.fa[x])
        return self.fa[x]

    def merge(self, x: int, y: int) -> None:
        root_x = self.get(x)
        root_y = self.get(y)
        if root_x != root_y:
            self.fa[root_x] = root_y
            self.cnt[root_y] += self.cnt[root_x]


if __name__ == "__main__":
    n, m = map(int, input().split())
    uf = UnionFind(n + 1)

    for _ in range(m):
        inputs = input().split()
        op = inputs[0]
        if op == 'C':
            a = int(inputs[1])
            b = int(inputs[2])
            if uf.get(a) != uf.get(b):
                uf.merge(a, b)
                
        elif op == 'Q1':
            a = int(inputs[1])
            b = int(inputs[2])
            print("Yes" if uf.get(a) == uf.get(b) else "No")
            
        elif op == 'Q2':
            a = int(inputs[1])
            print(uf.cnt[uf.get(a)])
