from typing import List

def interval_select(intervals: List[int]) -> int:
    intervals.sort(key=lambda x: x[1])
    points = []
    
    last_covered_end = float('-inf')
    
    for start, end in intervals:
        if start > last_covered_end:
            last_covered_end = end
            points.append(last_covered_end)
    
    return len(points)


if __name__ == "__main__":
    n = int(input())
    intervals = []
    for _ in range(n):
        a, b = map(int, input().split())
        intervals.append([a, b])
    
    ans = interval_select(intervals)
    print(ans)
