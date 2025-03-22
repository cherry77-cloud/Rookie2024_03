#include <iostream>
#include <string>
#include <vector>
using namespace std;


class StringHash {
private:
    using ULL = unsigned long long;
    string s;
    const ULL BASE = 13331;
    vector<ULL> prefix_hash;  // 存储字符串 s 的前缀哈希值，prefix_hash[i] 表示 s[0..i-1] 的哈希值
    vector<ULL> power;

    void precompute() {
        int n = s.size();
        prefix_hash.resize(n + 1);
        power.resize(n + 1);
        prefix_hash[0] = 0;
        power[0] = 1;
        for (int i = 1; i <= n; ++i) {
            power[i] = power[i - 1] * BASE;
            prefix_hash[i] = prefix_hash[i - 1] * BASE + s[i - 1]; // 自然溢出
        }
    }

public:
    StringHash(const string& str) : s(str) {
        precompute();
    }

    ULL getHash(int l, int r) {
        int len = r - l + 1;
        return prefix_hash[r + 1] - prefix_hash[l] * power[len];
    }

    bool compare(int l1, int r1, int l2, int r2) {
        if (r1 - l1 != r2 - l2) return false;
        return getHash(l1, r1) == getHash(l2, r2);
    }
};

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    string s;
    cin >> s;

    StringHash sh(s);

    while (m--) {
        int l1, r1, l2, r2;
        cin >> l1 >> r1 >> l2 >> r2;
        l1 -= 1; l2 -= 1; r1 -= 1; r2 -= 1;
        cout << (sh.compare(l1, r1, l2, r2) ? "Yes" : "No") << '\n';
    }

    return 0;
}
