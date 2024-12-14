from typing import List
import random

def quick_select(arr: List[int], low: int, high: int, k: int) -> int:
    if low >= high:
        return arr[low]
    
    pivot = arr[random.randint(low, high)]
    i, j = low, high

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
    left_part_size = j - low + 1
    if k <= left_part_size:
        return quick_select(arr, low, j, k)
    else:
        return quick_select(arr, j + 1, high, k - left_part_size)


if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(quick_select(nums, 0, n - 1, k))
