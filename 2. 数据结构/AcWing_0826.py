class LinkedList:
    def __init__(self, max_size=10**6+5) -> None:
        self.e = [0] * max_size  # 存储节点的值
        self.ne = [-1] * max_size  # 存储下一个节点的索引
        self.head = -1  # 头节点索引
        self.idx = 0  # 当前可用的节点索引

    def insert_head(self, x: int) -> None:
        self.e[self.idx] = x
        self.ne[self.idx] = self.head
        self.head = self.idx
        self.idx += 1

    def remove(self, k: int) -> None:
        if k == 0:
            self.head = self.ne[self.head]
        else:
            self.ne[k-1] = self.ne[self.ne[k-1]]

    def insert(self, k: int, x: int) -> None:
        self.e[self.idx] = x
        self.ne[self.idx] = self.ne[k-1]
        self.ne[k-1] = self.idx
        self.idx += 1

    def print_list(self) -> None:
        i = self.head
        while i != -1:
            print(self.e[i], end=' ')
            i = self.ne[i]
        print()

def main():
    M = int(input())
    linked_list = LinkedList()

    for _ in range(M):
        op = input().split()
        if op[0] == 'H':
            x = int(op[1])
            linked_list.insert_head(x)
        elif op[0] == 'D':
            k = int(op[1])
            linked_list.remove(k)
        elif op[0] == 'I':
            k, x = int(op[1]), int(op[2])
            linked_list.insert(k, x)

    linked_list.print_list()

if __name__ == "__main__":
    main()
