from collections import deque
from typing import List, Tuple

def spfa(n: int, edges: List[Tuple[int, int, int]]) -> bool:
    adj = [[] for _ in range(n + 1)]
    dist = [float('inf')] * (n + 1)
    cnt = [0] * (n + 1)
    vis = [False] * (n + 1)

    for x, y, z in edges:
        adj[x].append((y, z))

    queue = deque(range(1, n + 1))
    for i in range(1, n + 1):
        dist[i] = 0
        vis[i] = True

    while queue:
        x = queue.popleft()
        vis[x] = False
        for y, z in adj[x]:
            if dist[y] > dist[x] + z:
                dist[y] = dist[x] + z
                cnt[y] = cnt[x] + 1
                if cnt[y] >= n:
                    return True
                if not vis[y]:
                    queue.append(y)
                    vis[y] = True

    return False


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        x, y, z = map(int, input().split())
        edges.append((x, y, z))

    has_negative_cycle = spfa(n, edges)
    print("Yes" if has_negative_cycle else "No")
