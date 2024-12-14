from typing import List

def foo(list1: List[int], list2: List[int]) -> bool:
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        else:
            j += 1
    return i == len(list1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    
    if foo(list1, list2):
        print("Yes")
    else:
        print("No")
