from typing import List

def foo(nums: List[int]) -> List[int]:
    stack = []
    ans = [-1] * len(nums)
    
    for idx, x in enumerate(nums):
        while stack and nums[stack[-1]] >= x:
            stack.pop()
        ans[idx] = nums[stack[-1]] if stack else -1
        stack.append(idx)
    
    return ans


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    
    ans = foo(nums)
    
    for x in ans:
        print(x, end=" ")
