from typing import List
from collections import deque


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    ans = []
    q = deque()
    for i, x in enumerate(nums):
        while q and nums[q[-1]] <= x:
            q.pop()
        q.append(i)
        if i - q[0] >= k:
            q.popleft()
        if i >= k - 1:
            ans.append(nums[q[0]])
    return ans


def minSlidingWindow(nums: List[int], k: int) -> List[int]:
    ans = []
    q = deque()
    for i, x in enumerate(nums):
        while q and nums[q[-1]] >= x:
            q.pop()
        q.append(i)
        if i - q[0] >= k:
            q.popleft()
        if i >= k - 1:
            ans.append(nums[q[0]])
    return ans


if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    ans1 = minSlidingWindow(nums, k)
    ans2 = maxSlidingWindow(nums, k)
    
    for x in ans1:
        print(x, end=" ")
    
    print()
    
    for x in ans2:
        print(x, end=" ")
