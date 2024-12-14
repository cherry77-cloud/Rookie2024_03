from typing import List

def find_first_blue(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        pivot = (left + right) // 2
        if nums[pivot] >= target:
            right = pivot
        else:
            left = pivot + 1
    return left


def find_last_red(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        pivot = (left + right + 1) // 2
        if nums[pivot] <= target:
            left = pivot
        else:
            right = pivot - 1
    return left
    
    
if __name__ == "__main__":
    n, t = map(int, input().split())
    nums = list(map(int, input().split()))
    for _ in range(t):
        x = int(input())
        l = find_first_blue(nums, x)
        r = find_last_red(nums, x)
        if nums[l] != x:
            print("-1 -1")
        else:
            print(f"{l} {r}")
