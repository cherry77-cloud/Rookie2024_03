from typing import List, Tuple

def minimize_stack_risk(items: List[Tuple[int, int]]) -> int:
    items = [(weight + strength, weight) for weight, strength in items]
    items.sort()

    max_risk = -float('inf')
    total_weight = 0

    for total, weight in items:
        strength = total - weight
        risk = total_weight - strength
        max_risk = max(max_risk, risk)
        total_weight += weight

    return max_risk

    

if __name__ == "__main__":
    n = int(input())
    cows = []
    for _ in range(n):
        a, b = map(int, input().split())
        cows.append([a, b])
    print(minimize_stack_risk(cows))
