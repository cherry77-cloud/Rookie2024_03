from typing import List, Union, Tuple
from collections import deque

def topological_sort(n: int, edges: List[Tuple[int, int]]) -> Union[str, List[int]]:
    indegrees = [0] * (n + 1)
    adjacency = [[] for _ in range(n + 1)]
    
    for x, y in edges:
        indegrees[y] += 1
        adjacency[x].append(y)
    
    queue = deque([i for i in range(1, n + 1) if indegrees[i] == 0])
    if not queue:
        return "-1"
    
    topological_order = []
    
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        for neighbor in adjacency[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
    
    return topological_order if len(topological_order) == n else "-1"


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    result = topological_sort(n, edges)
    print(' '.join(map(str, result)) if isinstance(result, list) else result)
