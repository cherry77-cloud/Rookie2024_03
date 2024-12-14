from typing import List

def dijkstra(n: int, edges: List[List[int]]) -> int:
    graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0
    for u, v, w in edges:
        graph[u][v] = min(graph[u][v], w)
    
    dist = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)
    dist[1] = 0
    
    for _ in range(1, n):
        x = 0
        for i in range(1, n + 1):
            if not visited[i] and (x == 0 or dist[i] < dist[x]):
                x = i
        visited[x] = True
        
        for y in range(1, n + 1):
            dist[y] = min(dist[y], dist[x] + graph[x][y])
    
    return dist[n] if dist[n] != float('inf') else -1


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    result = dijkstra(n, edges)
    print(result)


if __name__ == "__main__":
    main()
