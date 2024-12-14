from typing import List

class ChainedHashTable:
    def __init__(self, capacity: int = 1000003) -> int:
        self.capacity = capacity  # 容量
        self.head = [-1] * capacity  # 链表头指针
        self.e = []  # 存储元素
        self.ne = []  # 存储下一个元素的索引
        self.tot = 0  # 目前存储的元素数量

    def _hash(self, key: int) -> int:
        return (key % self.capacity + self.capacity) % self.capacity

    def insert(self, key: int) -> None:
        idx = self._hash(key)
        i = self.head[idx]
        while i != -1:
            if self.e[i] == key:
                return
            i = self.ne[i]
        self.e.append(key)
        self.ne.append(self.head[idx])
        self.head[idx] = self.tot
        self.tot += 1

    def query(self, key: int) -> bool:
        idx = self._hash(key)
        i = self.head[idx]
        while i != -1:
            if self.e[i] == key:
                return True
            i = self.ne[i]
        return False


def main():
    hash_table = ChainedHashTable()
    n = int(input(""))
    for _ in range(n):
        operation, number = input().split()
        number = int(number)
        if operation == 'I':
            hash_table.insert(number)
        elif operation == 'Q':
            print("Yes" if hash_table.query(number) else "No")


if __name__ == "__main__":
    main()
