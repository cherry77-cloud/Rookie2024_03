import heapq
from typing import List, Tuple


def dijkstra(n: int, edges: List[Tuple[int, int, int]]) -> int:
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
    
    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]  # (distance, node)

    while pq:
        d, node = heapq.heappop(pq)
        if node == n:
            return d
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return -1


def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    
    result = dijkstra(n, edges)
    print(result)


if __name__ == "__main__":
    main()
