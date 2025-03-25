#include <iostream>
#include <vector>
#include <climits>

using namespace std;

const int INF = 0x3f3f3f3f;

struct Edge {
    int from, to, weight;
};

int BellmanFord(const vector<Edge>& edges, int n, int k) {
    vector<int> dist(n, INF);
    dist[0] = 0;

    for (int i = 0; i < k; ++i) {
        vector<int> backup = dist;
        bool updated = false;
        for (const auto& e : edges) {
            if (backup[e.from] != INF && dist[e.to] > backup[e.from] + e.weight) {
                dist[e.to] = backup[e.from] + e.weight;
                updated = true;
            }
        }
        if (!updated) break;
    }

    return dist[n-1];
}

int main() {
    int n, m, k;
    cin >> n >> m >> k;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        edges[i] = {u-1, v-1, w};
    }

    int ans = BellmanFord(edges, n, k);
    if (ans > INF / 2) {
        cout << "impossible" << endl;
    } else {
        cout << ans << endl;
    }

    return 0;
}
