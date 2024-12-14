from collections import deque
from typing import List, Tuple

def bfs_maze(n: int, m: int, grid: List[List[int]]) -> int:
    dist = [[-1] * m for _ in range(n)]
    queue = deque([(0, 0)])
    dist[0][0] = 0
    
    def neighbor(x: int, y: int) -> Tuple[int, int]:
        for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
            if 0 <= dx < n and 0 <= dy < m:
                yield dx, dy
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in neighbor(x, y):
            if grid[dx][dy] == 0 and dist[dx][dy] == -1:
                dist[dx][dy] = dist[x][y] + 1
                queue.append((dx, dy))
    
    return dist[n - 1][m - 1]


if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    
    print(bfs_maze(n, m, grid))
