from typing import List
from collections import defaultdict


def foo(nums: List[int]) -> int:
    left = 0
    ans = 0
    cnt = defaultdict(int)
    for right, x in enumerate(nums):
        cnt[x] += 1
        while left <= right and cnt[x] >= 2:
            cnt[nums[left]] -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(foo(nums))
