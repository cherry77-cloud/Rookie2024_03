from typing import List

def merge_sort(nums: List[int], low: int, high: int) -> None:
    if low == high:
        return

    mid = (low + high) // 2
    merge_sort(nums, low, mid)
    merge_sort(nums, mid + 1, high)

    merged = []
    i, j = low, mid + 1
    for k in range(low, high + 1):
        if j > high or (i <= mid and nums[i] <= nums[j]):
            merged.append(nums[i])
            i += 1
        else:
            merged.append(nums[j])
            j += 1
            
    nums[low:high+1] = merged


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    merge_sort(nums, 0, n - 1)
    for num in nums:
        print(num, end=' ')


if __name__ == "__main__":
    main()
