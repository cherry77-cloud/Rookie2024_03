from bisect import bisect_left
from typing import List

def greedy_largets_increasing_seq(nums: List[int]) -> int:
    tails = []
    for num in nums:
        idx = bisect_left(tails, num)  # 使用二分查找确定插入位置
        if idx == len(tails):          # 如果是新的更长序列，添加到末尾
            tails.append(num)
        else:
            tails[idx] = num           # 否则更新存在的位置
    return len(tails)                  # 返回最长上升子序列的长度


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(greedy_largets_increasing_seq(nums))
