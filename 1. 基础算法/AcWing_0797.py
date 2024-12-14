import itertools
from typing import List


class DiffArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.diff = [0] * (self.n + 1)
        self.diff[0] = nums[0]
        for i in range(1, self.n):
            self.diff[i] = nums[i] - nums[i - 1]

    def update(self, from_: int, to: int, val: int) -> None:
        self.diff[from_] += val
        if to + 1 < self.n:
            self.diff[to + 1] -= val

    def reconstruct(self) -> List[int]:
        return list(itertools.accumulate(self.diff[:self.n]))


def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    diff_array = DiffArray(nums)

    for _ in range(m):
        l, r, val = map(int, input().split())
        diff_array.update(l - 1, r - 1, val)

    final_array = diff_array.reconstruct()
    print(" ".join(map(str, final_array)))


if __name__ == "__main__":
    main()
