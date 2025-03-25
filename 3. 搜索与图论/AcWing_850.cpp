#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

const int INF = 0x3f3f3f3f;

int dijkstra(const vector<vector<pair<int, int>>>& graph) {
    int n = graph.size();
    vector<int> dist(n, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;

    dist[0] = 0;
    pq.emplace(0, 0);

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (d > dist[u]) continue;

        for (auto [v, w] : graph[u]) {
            if (dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                pq.emplace(dist[v], v);
            }
        }
    }

    return dist[n-1] == INF ? -1 : dist[n-1];
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<pair<int, int>>> graph(n);

    while (m--) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u-1].emplace_back(v-1, w);
    }

    int ans = dijkstra(graph);
    cout << (ans == -1 ? -1 : ans) << endl;

    return 0;
}
