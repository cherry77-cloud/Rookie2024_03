from collections import deque
from typing import List, Tuple

def bipartite_check(n: int, edges: List[Tuple[int, int]]) -> bool:
    graph = [[] for _ in range(n + 1)]
    color = [0] * (n + 1)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start: int) -> bool:
        queue = deque([start])
        color[start] = 1
        while queue:
            node = queue.popleft()
            next_color = 1 if color[node] == 2 else 2
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True

    return all(bfs(i) if color[i] == 0 else True for i in range(1, n + 1))


def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    if bipartite_check(n, edges):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
