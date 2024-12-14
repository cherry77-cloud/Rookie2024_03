from typing import List, Tuple
from bisect import bisect_left


def foo(list1: List[int], list2: List[int]) -> Tuple[int, int]:
    for i in range(len(list1)):
        idx = bisect_left(list2, target - list1[i])
        if idx < len(list2) and list1[i] + list2[idx] == target:
            return (i, idx)
    return (-1, -1)


if __name__ == "__main__":
    n, m, target = map(int, input().split())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    i1, i2 = foo(list1, list2)
    print(i1, i2)
