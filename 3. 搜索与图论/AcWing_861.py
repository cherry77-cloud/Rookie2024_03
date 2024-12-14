from collections import deque
from typing import List, Tuple

def hopcroft_karp(n1: int, n2: int, edges: List[Tuple[int, int]]) -> int:
    adj = [[] for _ in range(n1 + 1)]
    pair_u = [-1] * (n1 + 1)
    pair_v = [-1] * (n2 + 1)
    dist = [-1] * (n1 + 1)

    for u, v in edges:
        adj[u].append(v)

    def bfs() -> bool:
        queue = deque([u for u in range(1, n1 + 1) if pair_u[u] == -1])
        for u in range(1, n1 + 1):
            dist[u] = 0 if pair_u[u] == -1 else -1
        found = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if pair_v[v] == -1:
                    found = True
                elif dist[pair_v[v]] == -1:
                    dist[pair_v[v]] = dist[u] + 1
                    queue.append(pair_v[v])
        return found

    def dfs(u: int) -> bool:
        for v in adj[u]:
            if pair_v[v] == -1 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                pair_u[u] = v
                pair_v[v] = u
                return True
        return False

    matching = 0
    while bfs():
        matching += sum(1 for u in range(1, n1 + 1) if pair_u[u] == -1 and dfs(u))
    return matching


if __name__ == "__main__":
    n1, n2, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(hopcroft_karp(n1, n2, edges))
