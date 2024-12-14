from collections import deque

def bfs(start: str) -> int:
    target = "12345678x"
    queue = deque([(start, 0)])
    seen = {start: 0}
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        state, dist = queue.popleft()
        
        if state == target:
            return dist
        
        idx = state.index('x')  # 找到 'x' 的位置
        x, y = divmod(idx, 3)  # 获取 'x' 在二维网格中的坐标
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                ni = nx * 3 + ny
                new_state = list(state)
                new_state[idx], new_state[ni] = new_state[ni], 'x'  # 交换位置
                new_state = ''.join(new_state)
                if new_state not in seen:
                    seen[new_state] = dist + 1
                    queue.append((new_state, dist + 1))
    
    return -1  # 如果没有解决方案，则返回 -1

if __name__ == "__main__":
    start = ''.join(input().strip().replace(' ', ''))
    result = bfs(start)
    print(result)
