from collections import deque, defaultdict
from typing import List, Tuple

def bfs(n: int, edges: List[Tuple[int, int]]) -> int:
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)

    dist = [None] * (n + 1)
    dist[1] = 0

    queue = deque([1])

    while queue:
        node = queue.popleft()
        current_distance = dist[node]

        for neighbor in graph[node]:
            if dist[neighbor] is None:
                queue.append(neighbor)
                dist[neighbor] = current_distance + 1

    return dist[n] if dist[n] is not None else -1


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        x, y = map(int, input().split())
        edges.append((x, y))

    result = bfs(n, edges)
    print(result)
