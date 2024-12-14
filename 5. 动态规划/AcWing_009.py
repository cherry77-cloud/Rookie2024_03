from typing import List, Tuple

def group_knapsack(max_capacity: int, groups_items: List[List[Tuple[int, int]]]) -> int:
    dp = [0] * (max_capacity + 1)
    for items in groups_items:
        for cur_capacity in range(max_capacity, -1, -1):
            for weight, value in items:
                if weight <= cur_capacity:
                    dp[cur_capacity] = max(dp[cur_capacity], dp[cur_capacity - weight] + value)

    return dp[max_capacity]


if __name__ == "__main__":
    num_groups, backpack_capacity = map(int, input().split())
    groups = []

    for _ in range(num_groups):
        num_items = int(input())
        current_group = []
        for _ in range(num_items):
            volume, value = map(int, input().split())
            current_group.append((volume, value))
        groups.append(current_group)

    max_value = group_knapsack(backpack_capacity, groups)
    print(max_value)
