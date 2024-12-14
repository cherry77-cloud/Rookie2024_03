from typing import List

def multiple_knapsack(capacity: int, weights: List[int], values: List[int], counts: List[int]) -> int:
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for mod in range(weights[i]):
            queue = []
            max_range = (capacity - mod) // weights[i]
            for k in range(max_range + 1):
                val = dp[k * weights[i] + mod] - k * values[i]
                
                while queue and queue[-1][1] <= val:
                    queue.pop()
                queue.append((k, val))
                
                if queue[0][0] < k - counts[i]:
                    queue.pop(0)
                
                dp[k * weights[i] + mod] = queue[0][1] + k * values[i]

    return dp[capacity]


if __name__ == "__main__":
    n, capacity = map(int, input().split())

    weights = []
    values = []
    counts = []
    
    for i in range(n):
        w, v, c = map(int, input().split())
        counts.append(c)
        values.append(v)
        weights.append(w)
        
    max_value = multiple_knapsack(capacity, weights, values, counts)
    print(max_value)
