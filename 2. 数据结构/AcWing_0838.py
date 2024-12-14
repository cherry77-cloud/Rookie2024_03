class MinHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.heap = [0] * (max_size + 1)  # 索引0不使用，从1开始

    def down(self, p):
        while True:
            rt = p
            if 2 * p <= self.size and self.heap[2 * p] < self.heap[rt]:
                rt = 2 * p
            if 2 * p + 1 <= self.size and self.heap[2 * p + 1] < self.heap[rt]:
                rt = 2 * p + 1
            if rt == p:
                break
            self.heap[p], self.heap[rt] = self.heap[rt], self.heap[p]
            p = rt

    def build_heap(self):
        for i in range(self.size // 2, 0, -1):
            self.down(i)

    def get_min(self):
        if self.size == 0:
            return None
        min_val = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.down(1)
        return min_val


def main():
    n, m = map(int, input().split())
    heap = MinHeap(n)
    heap.size = n
    heap.heap[1:] = list(map(int, input().split()))
    heap.build_heap()
    
    # 输出m次最小值
    result = []
    for _ in range(m):
        min_val = heap.get_min()
        if min_val is not None:
            result.append(str(min_val))
        else:
            break
    
    print(" ".join(result))

if __name__ == "__main__":
    main()
