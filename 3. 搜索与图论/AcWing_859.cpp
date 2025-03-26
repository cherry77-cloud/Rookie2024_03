#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

const int INF = 0x3f3f3f3f;

struct Edge {
    int u, v, w;
    bool operator<(const Edge& other) const {
        return w < other.w;
    }
};

int kruskal(vector<Edge>& edges, int n) {
    if (n <= 0) return INF;
    
    vector<int> parent(n);
    iota(parent.begin(), parent.end(), 0);
    
    auto find = [&](int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };

    sort(edges.begin(), edges.end());
    int total = 0, cnt = 0;

    for (const auto& [u, v, w] : edges) {
        int ru = find(u), rv = find(v);
        if (ru != rv) {
            parent[ru] = rv;
            total += w;
            if (++cnt == n - 1) break;
        }
    }

    return cnt == n - 1 ? total : INF;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    
    // 输入合法性检查
    if (n < 0 || m < 0) {
        cout << "impossible\n";
        return 0;
    }
    if (n == 1) {  // 单独处理单个节点的情况
        cout << (m == 0 ? "0" : "impossible") << "\n";
        return 0;
    }

    vector<Edge> edges;
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        u -= 1;
        v -= 1;
        edges.push_back({u, v, w});
    }

    int ans = kruskal(edges, n);
    cout << (ans == INF ? "impossible" : to_string(ans)) << "\n";
}
