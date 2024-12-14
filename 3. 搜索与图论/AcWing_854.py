def floyd_warshall(n: int, edges: list) -> list:
    # 初始化距离矩阵
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0

    # 建图
    for x, y, z in edges:
        dist[x][y] = min(dist[x][y], z)

    # Floyd-Warshall 算法进行所有点对的最短路径计算
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] < float('inf') and dist[k][j] < float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def process_queries(dist: list, queries: list) -> list:
    results = []
    for x, y in queries:
        if dist[x][y] == float('inf'):
            results.append("impossible")
        else:
            results.append(dist[x][y])
    return results


if __name__ == "__main__":
    n, m, Q = map(int, input().split())
    edges = []
    for _ in range(m):
        x, y, z = map(int, input().split())
        edges.append((x, y, z))
    
    queries = []
    for _ in range(Q):
        x, y = map(int, input().split())
        queries.append((x, y))
    
    # 执行 Floyd-Warshall 算法
    distance_matrix = floyd_warshall(n, edges)
    
    # 处理查询并打印结果
    results = process_queries(distance_matrix, queries)
    for result in results:
        print(result)
