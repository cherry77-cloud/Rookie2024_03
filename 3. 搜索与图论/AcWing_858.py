from typing import List, Tuple, Union
import heapq

def prim_optimized(n: int, edges: List[Tuple[int, int, int]]) -> Union[str, int]:
    g = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for x, y, z in edges:
        g[x][y] = g[y][x] = min(g[x][y], z)

    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    visited = [False] * (n + 1)
    min_heap = [(0, 1)]
    total_cost = 0

    while min_heap:
        cost, x = heapq.heappop(min_heap)
        
        if visited[x]:
            continue
        
        visited[x] = True
        total_cost += cost

        for y in range(1, n + 1):
            if not visited[y] and g[x][y] < dist[y]:
                dist[y] = g[x][y]
                heapq.heappush(min_heap, (dist[y], y))

    return total_cost if all(visited[1:]) else "impossible"


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    result = prim_optimized(n, edges)
    print(result)
