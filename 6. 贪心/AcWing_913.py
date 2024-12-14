from typing import List

def minimize_total_wait(times: List[int]) -> int:
    times.sort()
    total_waiting_time = 0
    current_wait = 0
    for time in times:
        total_waiting_time += current_wait
        current_wait += time
    return total_waiting_time


if __name__ == "__main__":
    n = int(input())
    times = list(map(int, input().split()))
    print(minimize_total_wait(times))
