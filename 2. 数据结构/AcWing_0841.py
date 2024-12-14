class DoubleHash:
    def __init__(self, s: str):
        self.s = s
        self.P1 = 13331
        self.P2 = 131
        self.MOD1 = 10**9 + 7
        self.MOD2 = 10**9 + 9
        self.n = len(s)
        self.h1 = [0] * (self.n + 1)
        self.h2 = [0] * (self.n + 1)
        self.p1 = [1] * (self.n + 1)
        self.p2 = [1] * (self.n + 1)
        self._precompute()

    def _precompute(self):
        for i in range(1, self.n + 1):
            self.p1[i] = self.p1[i - 1] * self.P1 % self.MOD1
            self.p2[i] = self.p2[i - 1] * self.P2 % self.MOD2
            self.h1[i] = (self.h1[i - 1] * self.P1 + ord(self.s[i - 1])) % self.MOD1
            self.h2[i] = (self.h2[i - 1] * self.P2 + ord(self.s[i - 1])) % self.MOD2

    def get_hash(self, l: int, r: int):
        hash1 = (self.h1[r] - self.h1[l - 1] * self.p1[r - l + 1] % self.MOD1 + self.MOD1) % self.MOD1
        hash2 = (self.h2[r] - self.h2[l - 1] * self.p2[r - l + 1] % self.MOD2 + self.MOD2) % self.MOD2
        return (hash1, hash2)

    def compare_substrings(self, l1: int, r1: int, l2: int, r2: int) -> bool:
        return self.get_hash(l1, r1) == self.get_hash(l2, r2)

def main():
    n, m = map(int, input().split())
    s = input()
    double_hash = DoubleHash(s)
    
    for _ in range(m):
        l1, r1, l2, r2 = map(int, input().split())
        if double_hash.compare_substrings(l1, r1, l2, r2):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
