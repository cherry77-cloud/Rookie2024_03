from typing import List

def multiple_knapsack(capacity: int, weights: List[int], values: List[int], counts: List[int]) -> int:
    n = len(weights)
    items = []

    # 二进制拆分物品
    for i in range(n):
        k = 1
        while k <= counts[i]:
            items.append((weights[i] * k, values[i] * k))
            counts[i] -= k
            k *= 2
        if counts[i] > 0:
            items.append((weights[i] * counts[i], values[i] * counts[i]))

    dp = [0] * (capacity + 1)

    for weight, value in items:
        for j in range(capacity, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)

    return dp[capacity]


if __name__ == "__main__":
    n, capacity = map(int, input().split())
    
    volumes = []
    weights = []
    counts = []
    
    for i in range(n):
        v, w, c = map(int, input().split())
        counts.append(c)
        volumes.append(v)
        weights.append(w)
        
    max_value = multiple_knapsack(capacity, volumes, weights, counts)
    print(max_value)
