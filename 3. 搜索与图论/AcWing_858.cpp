#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

const int INF = INT_MAX;

int prim(const vector<vector<int>>& g) {
    int n = g.size();
    vector<int> dist(n, INF);
    vector<bool> vis(n, false);
    priority_queue<pair<int, int>> pq;

    dist[0] = 0;
    pq.push({0, 0});

    int total_weight = 0;
    int nodes_in_mst = 0;

    while (!pq.empty()) {
        int u = pq.top().second;
        int d = -pq.top().first;
        pq.pop();

        if (vis[u]) continue;
        vis[u] = true;
        total_weight += d;
        nodes_in_mst++;

        for (int v = 0; v < n; ++v) {
            if (g[u][v] != 0 && !vis[v] && g[u][v] < dist[v]) {
                dist[v] = g[u][v];
                pq.push({-dist[v], v});
            }
        }
    }

    return (nodes_in_mst == n) ? total_weight : INF;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> g(n, vector<int>(n, INF));
    for (int i = 0; i < n; ++i) g[i][i] = 0;

    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        u--; v--; // 转换为0-based
        if (g[u][v] > w) {
            g[u][v] = w;
            g[v][u] = w;
        }
    }

    int res = prim(g);
    if (res == INF)
        cout << "impossible" << endl;
    else
        cout << res << endl;

    return 0;
}
