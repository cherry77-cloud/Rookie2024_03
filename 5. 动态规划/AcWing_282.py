from typing import List

def merge_stones(stones: List[int]) -> int:
    num_stones = len(stones)
    prefix_sum = [0] * (num_stones + 1)
    dp = [[float('inf')] * (num_stones + 1) for _ in range(num_stones + 1)]

    for i in range(1, num_stones + 1):
        prefix_sum[i] = prefix_sum[i - 1] + stones[i - 1]

    for i in range(1, num_stones + 1):
        dp[i][i] = 0

    for length in range(2, num_stones + 1):  # 枚举区间长度
        for l in range(1, num_stones - length + 2):  # 枚举区间起点
            r = l + length - 1
            for k in range(l, r):  # 枚举分割点，计算最小成本
                dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r] + prefix_sum[r] - prefix_sum[l - 1])

    return dp[1][num_stones]


if __name__ == "__main__":
    n = int(input())
    stones = list(map(int, input().split()))
    print(merge_stones(stones))
