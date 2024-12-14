from typing import List, Tuple, Union
import heapq

def kruskal(n: int, edges: List[Tuple[int, int, int]]) -> Union[int, str]:
    parent = list(range(n + 1))
    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    edges.sort(key=lambda x: x[2])
    mst_cost = 0
    edges_used = 0
    
    for x, y, z in edges:
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_x] = root_y
            mst_cost += z
            edges_used += 1
            if edges_used == n - 1:
                break
    
    return mst_cost if edges_used == n - 1 else "impossible"


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    result = kruskal(n, edges)
    print(result)
