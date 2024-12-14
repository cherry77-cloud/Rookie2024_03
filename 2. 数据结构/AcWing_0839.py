class IndexedMinHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.tot = 0  # 堆中元素总数
        self.kth = 0  # 插入的第k个元素
        self.heap = [0] * (max_size + 1)  # 堆数组
        self.ph = [0] * (max_size + 1)    # 第k个插入的元素在堆中的位置
        self.hp = [0] * (max_size + 1)    # 堆中位置i的元素是第几个插入的

    def heap_swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
        self.hp[a], self.hp[b] = self.hp[b], self.hp[a]
        self.ph[self.hp[a]], self.ph[self.hp[b]] = a, b

    def up(self, p):
        while p // 2 > 0 and self.heap[p] < self.heap[p // 2]:
            self.heap_swap(p, p // 2)
            p //= 2

    def down(self, u):
        rt = u
        if 2 * u <= self.tot and self.heap[2 * u] < self.heap[rt]:
            rt = 2 * u
        if 2 * u + 1 <= self.tot and self.heap[2 * u + 1] < self.heap[rt]:
            rt = 2 * u + 1
        if rt != u:
            self.heap_swap(rt, u)
            self.down(rt)

    def insert(self, x):
        self.tot += 1
        self.kth += 1
        self.heap[self.tot] = x
        self.hp[self.tot] = self.kth
        self.ph[self.kth] = self.tot
        self.up(self.tot)

    def get_min(self):
        return self.heap[1]

    def delete_min(self):
        self.heap_swap(1, self.tot)
        self.tot -= 1
        self.down(1)

    def delete(self, k):
        pos = self.ph[k]
        self.heap_swap(pos, self.tot)
        self.tot -= 1
        self.up(pos)
        self.down(pos)

    def change(self, k, x):
        pos = self.ph[k]
        self.heap[pos] = x
        self.up(pos)
        self.down(pos)

def main():
    n = int(input())
    heap = IndexedMinHeap(100010)

    for _ in range(n):
        op = input().split()

        if op[0] == "I":
            x = int(op[1])
            heap.insert(x)

        elif op[0] == "PM":
            print(heap.get_min())

        elif op[0] == "DM":
            heap.delete_min()

        elif op[0] == "D":
            k = int(op[1])
            heap.delete(k)

        elif op[0] == "C":
            k, x = int(op[1]), int(op[2])
            heap.change(k, x)

if __name__ == "__main__":
    main()
