#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

const int INF = 0x3f3f3f3f;

int SPFA(const vector<vector<pair<int, int>>>& graph) {
    int n = graph.size();
    vector<int> dist(n, INF);
    vector<bool> in_queue(n, false);
    queue<int> q;

    dist[0] = 0; // 起点为0
    q.push(0);
    in_queue[0] = true;

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        in_queue[u] = false;

        for (const auto& [v, w] : graph[u]) {
            if (dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                if (!in_queue[v]) {
                    q.push(v);
                    in_queue[v] = true;
                }
            }
        }
    }

    return dist.back();
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<pair<int, int>>> graph(n);
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u-1].emplace_back(v-1, w); // 转换为0-based
    }

    int ans = SPFA(graph);
    if (ans == INF) {
        cout << "impossible" << endl;
    } else {
        cout << ans << endl;
    }

    return 0;
}
