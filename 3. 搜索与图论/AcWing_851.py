from typing import List, Tuple, Union
from collections import deque

def spfa(n: int, edges: List[Tuple[int, int, int]]) -> Union[str, int]:
    # 初始化邻接表
    adj_list = [[] for _ in range(n + 1)]
    dist = [float('inf')] * (n + 1)
    in_queue = [False] * (n + 1)

    # 建图
    for x, y, z in edges:
        adj_list[x].append((y, z))

    # 初始化队列和起点距离
    queue = deque([1])
    dist[1] = 0
    in_queue[1] = True

    while queue:
        x = queue.popleft()
        in_queue[x] = False
        for y, z in adj_list[x]:
            if dist[y] > dist[x] + z:
                dist[y] = dist[x] + z
                if not in_queue[y]:
                    queue.append(y)
                    in_queue[y] = True

    # 检查是否可以到达节点 n
    return dist[n] if dist[n] != float('inf') else "impossible"

if __name__ == "__main__":
    num_vertices, num_edges = map(int, input().split())
    edges = []
    for _ in range(num_edges):
        edges.append(tuple(map(int, input().split())))
    
    result = spfa(num_vertices, edges)
    print(result)
