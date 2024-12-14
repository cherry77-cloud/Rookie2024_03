class DoublyLinkedList:
    def __init__(self, max_size=10**5+10) -> None:
        self.max_size = max_size
        self.e = [0] * max_size  # 存储节点的值
        self.l = [0] * max_size  # 存储左侧节点的索引
        self.r = [0] * max_size  # 存储右侧节点的索引
        self.idx = 2  # 当前可用的节点索引，从2开始，因为0和1用作头尾哨兵
        self.initialize()

    def initialize(self) -> None:
        # 0是左端点，1是右端点
        self.r[0] = 1
        self.l[1] = 0

    def insert(self, k: int, x: int) -> None:
        self.e[self.idx] = x
        self.r[self.idx] = self.r[k]
        self.l[self.idx] = k
        self.l[self.r[k]] = self.idx
        self.r[k] = self.idx
        self.idx += 1

    def remove(self, k: int) -> None:
        self.r[self.l[k]] = self.r[k]
        self.l[self.r[k]] = self.l[k]

    def print_list(self) -> None:
        i = self.r[0]
        while i != 1:
            print(self.e[i], end=' ')
            i = self.r[i]
        print()

def main():
    M = int(input())
    linked_list = DoublyLinkedList()

    for i in range(1, M+1):
        op = input().split()
        
        if op[0] == 'L':
            x = int(op[1])
            linked_list.insert(0, x)
        
        elif op[0] == 'R':
            x = int(op[1])
            linked_list.insert(linked_list.l[1], x)
        
        elif op[0] == 'D':
            k = int(op[1])
            linked_list.remove(k + 1)  # +1是因为真实的索引从2开始
        
        elif op[0] == 'IL':
            k, x = int(op[1]), int(op[2])
            linked_list.insert(linked_list.l[k + 1], x)
        
        elif op[0] == 'IR':
            k, x = int(op[1]), int(op[2])
            linked_list.insert(k + 1, x)

    linked_list.print_list()

if __name__ == "__main__":
    main()
