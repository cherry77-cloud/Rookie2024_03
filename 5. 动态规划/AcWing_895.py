from typing import List

def lengthOfLIS(arr: List[int]) -> int:
    n = len(arr)
    dp = [1] * n  # dp[i] 存储以 arr[i] 结尾的最长递增子序列的长度

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # 返回整个数组中最大的 LIS 长度


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(lengthOfLIS(nums))
