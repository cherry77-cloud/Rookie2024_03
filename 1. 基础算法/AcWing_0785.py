from typing import List
import random


def quick_sort(arr: List[int], low: int, high: int) -> None:
    if low >= high:
        return
    
    i, j = low, high
    pivot = arr[random.randint(low, high)]
    
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    quick_sort(arr, low, j)
    quick_sort(arr, j + 1, high)


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    quick_sort(nums, 0, len(nums) - 1)
    print(" ".join(map(str, nums)))
