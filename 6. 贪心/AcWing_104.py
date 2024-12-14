from typing import List

def optimal_warehouse_location(shops: List[int]) -> int:
    shops.sort()
    total_distance = 0
    for i in range(len(shops)):
        total_distance += shops[i] - shops[i >> 1]
        
    return total_distance


if __name__ == "__main__":
    n = int(input())
    shops = list(map(int, input().split()))
    print(optimal_warehouse_location(shops))
