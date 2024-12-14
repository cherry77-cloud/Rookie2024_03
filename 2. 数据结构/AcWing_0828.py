def simulate_stack_operations():
    n = int(input())  # 读取操作的数量
    stack = []
    
    for _ in range(n):
        parts = input().split()
        op = parts[0]
        
        if op == "push":
            x = int(parts[1])
            stack.append(x)
        
        elif op == "pop":
            if stack:
                stack.pop()
        
        elif op == "query":
            if stack:
                print(stack[-1])
        
        elif op == "empty":
            if not stack:
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    simulate_stack_operations()
