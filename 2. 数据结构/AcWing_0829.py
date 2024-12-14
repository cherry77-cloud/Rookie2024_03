from collections import deque

def main():
    n = int(input())  # 读取操作的数量
    queue = deque()   # 创建一个双端队列

    for _ in range(n):
        command = input().split()
        op = command[0]
        
        if op == "push":
            x = int(command[1])
            queue.append(x)
        elif op == "pop":
            if queue:
                queue.popleft()
        elif op == "query":
            if queue:
                print(queue[0])
        else:  # empty 操作
            print("NO" if queue else "YES")


if __name__ == "__main__":
    main()
