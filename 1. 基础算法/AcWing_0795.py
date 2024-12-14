from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        # s = list(accumulate(nums, initial=0))
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x
        self.s = s

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]


if __name__ == "__main__":
    n, q = map(int, input().split())
    s = list(map(int, input().split()))
    
    pre_sum = NumArray(s);
    
    for _ in range(q):
        l, r = map(int, input().split())
        print(pre_sum.sumRange(l - 1, r - 1))
