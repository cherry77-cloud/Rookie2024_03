from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda p: p[0])  # 按照左端点从小到大排序
    ans = []
    for p in intervals:
        if ans and p[0] <= ans[-1][1]:  # 可以合并
            ans[-1][1] = max(ans[-1][1], p[1])  # 更新右端点最大值
        else:  # 不相交，无法合并
            ans.append(p)  # 新的合并区间
    return ans


if __name__ == "__main__":
    n = int(input())
    intervals = []
    
    for _ in range(n):
        a, b = map(int, input().split())
        intervals.append([a, b])
    
    ans = merge(intervals)
    print(len(ans))
