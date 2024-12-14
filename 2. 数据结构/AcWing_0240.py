class UnionFind:
    def __init__(self, size):
        self.fa = list(range(size))

    def get(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.get(self.fa[x])
        return self.fa[x]

    def merge(self, x, y):
        self.fa[self.get(x)] = self.get(y)


if __name__ == "__main__":
    n, k = map(int, input().split())
    uf = UnionFind(3 * n + 1)  # 创建一个足够大的并查集

    fake = 0
    for _ in range(k):
        op, x, y = map(int, input().split())
        if x > n or y > n:
            fake += 1
            continue
        
        x_self, x_eat, x_enemy = x, x + n, x + 2 * n
        y_self, y_eat, y_enemy = y, y + n, y + 2 * n
        
        if op == 1:
            if uf.get(x_eat) == uf.get(y_self) or uf.get(x_self) == uf.get(y_eat):
                fake += 1
            else:
                uf.merge(x_self, y_self)
                uf.merge(x_eat, y_eat)
                uf.merge(x_enemy, y_enemy)
        
        elif op == 2:
            if uf.get(x_self) == uf.get(y_self) or uf.get(x_self) == uf.get(y_eat):
                fake += 1
            else:
                uf.merge(x_eat, y_self)
                uf.merge(x_self, y_enemy)
                uf.merge(x_enemy, y_eat)

    print(fake)
