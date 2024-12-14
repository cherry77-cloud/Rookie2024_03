from typing import List, Tuple
from collections import defaultdict, deque

def find_tree_centroid(n: int, edges: List[Tuple[int, int]]) -> int:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    subtree_sizes = [0] * (n + 1)

    def dfs(node: int, parent: int) -> int:
        subtree_size = 1
        max_subtree_size = 0
        for neighbor in graph[node]:
            if neighbor != parent:
                neighbor_size = dfs(neighbor, node)
                subtree_size += neighbor_size
                max_subtree_size = max(max_subtree_size, neighbor_size)

        max_subtree_size = max(max_subtree_size, n - subtree_size)
        subtree_sizes[node] = max_subtree_size
        return subtree_size

    dfs(1, -1)

    return min(subtree_sizes[1:])


if __name__ == "__main__":
    n = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    result = find_tree_centroid(n, edges)
    print(result)
