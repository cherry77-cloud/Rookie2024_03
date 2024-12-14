from typing import List

def huffman_tree_cost(numbers: List[int]) -> int:
    import heapq
    heapq.heapify(numbers)
    total_cost = 0
    while len(numbers) > 1:
        first_min = heapq.heappop(numbers)
        second_min = heapq.heappop(numbers)
        total_cost += first_min + second_min
        heapq.heappush(numbers, first_min + second_min)
    return total_cost


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    print(huffman_tree_cost(numbers))
