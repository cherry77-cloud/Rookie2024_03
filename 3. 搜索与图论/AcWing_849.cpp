#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

constexpr int INF = 0x3f3f3f3f;


int dijkstra(const vector<vector<int>>& g, int n) {
    vector<int> dist(n + 1, INF);
    vector<bool> visited(n + 1, false);
    dist[1] = 0;
    
    for (int i = 1; i < n; ++i) {
        int u = 0;
        for (int j = 1; j <= n; ++j) {
            if (!visited[j] && (u == 0 || dist[j] < dist[u])) {
                u = j;
            }
        }
        
        if (u == 0 || dist[u] == INF) break;
        visited[u] = true;
        
        for (int v = 1; v <= n; ++v) {
            dist[v] = min(dist[v], dist[u] + g[u][v]);
        }
    }
    
    return dist[n] == INF ? -1 : dist[n];
}

int main() {
    int n, m;
    cin >> n >> m;
    
    vector<vector<int>> g(n + 1, vector<int>(n + 1, INF));
    for (int i = 1; i <= n; ++i) {
        g[i][i] = 0;
    }
    
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        g[u][v] = min(g[u][v], w);
    }
    
    int shortest = dijkstra(g, n);
    cout << shortest << endl;
    
    return 0;
}
