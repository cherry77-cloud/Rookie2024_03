from typing import List, Tuple, Union


def bellman_ford(num_vertices: int, max_iterations: int, edges: List[Tuple[int, int, int]]) -> Union[str, int]:
    dist = [float('inf')] * (num_vertices + 1)
    dist[1] = 0

    for _ in range(max_iterations):
        new_dist = dist[:]
        for x, y, z in edges:
            dist[y] = min(dist[y], new_dist[x] + z)

    return dist[num_vertices] if dist[num_vertices] != float('inf') else "impossible"


if __name__ == "__main__":
    num_vertices, num_edges, max_iterations = map(int, input().split())
    edges = []
    for _ in range(num_edges):
        x, y, z = map(int, input().split())
        edges.append((x, y, z))
    
    result = bellman_ford(num_vertices, max_iterations, edges)
    print(result)
