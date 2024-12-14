from typing import List


def zero_one_knapsack(capacity: int, weights: List[int], values: List[int]) -> int:
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return max(dp)


if __name__ == "__main__":
    n, capacity = map(int, input().split())

    weights = []
    values = []

    for i in range(n):
        w, v = map(int, input().split())
        weights.append(w)
        values.append(v)

    max_value = zero_one_knapsack(capacity, weights, values)
    print(max_value)
