from typing import List, Tuple

def interval_coverage(start: int, end: int, intervals: List[Tuple[int, int]]) -> int:
    if start == end:
        return 1 if any(a <= start <= b for a, b in intervals) else -1
    
    intervals = [x for x in intervals if x[0] <= end and x[1] >= start]
    intervals.sort(key=lambda x: (x[0], -x[1]))
    
    count = 0
    current_end = start
    
    i = 0
    while current_end < end:
        max_end = current_end
        while i < len(intervals) and intervals[i][0] <= current_end:
            max_end = max(max_end, intervals[i][1])
            i += 1
            
        if max_end == current_end:
            return -1
        
        current_end = max_end
        count += 1
        
    return count


if __name__ == "__main__":
    start, end = map(int, input().split())
    n = int(input())
    intervals = []
    for _ in range(n):
        a, b = map(int, input().split())
        intervals.append((a, b))
    print(interval_coverage(start, end, intervals))
