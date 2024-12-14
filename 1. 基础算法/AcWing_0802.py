from bisect import bisect_left
from collections import defaultdict

def main():
    n, m = map(int, input().split())
    
    events = []
    queries = []
    all_values = set()
    
    for _ in range(n):
        x, c = map(int, input().split())
        events.append((x, c))
        all_values.add(x)
    
    for _ in range(m):
        l, r = map(int, input().split())
        queries.append((l, r))
        all_values.add(l)
        all_values.add(r)
    
    
    sorted_values = sorted(all_values)
    index_map = {value: idx for idx, value in enumerate(sorted_values)}
    
    # 使用数组处理累加和
    a = [0] * (len(sorted_values) + 1)
    
    # 更新事件
    for x, c in events:
        a[index_map[x]] += c
    
    # 计算前缀和
    s = [0] * (len(sorted_values) + 1)
    for i in range(0, len(sorted_values)):
        s[i + 1] = s[i] + a[i]
    
    # 处理每个查询
    results = []
    for l, r in queries:
        l_idx = index_map[l]
        r_idx = index_map[r]
        result = s[r_idx + 1] - s[l_idx]
        results.append(result)
    
    # 输出结果
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
