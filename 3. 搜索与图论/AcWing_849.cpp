#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

constexpr int INF = 0x3f3f3f3f;

int dijkstra(const vector<vector<int>>& g) {
    int n = g.size();
    vector<int> dist(n, INF);
    vector<bool> visited(n, false);
    
    dist[0] = 0;
    
    for (int i = 0; i < n - 1; ++i) {
        int u = -1;
        for (int j = 0; j < n; ++j) {
            if (!visited[j] && (u == -1 || dist[j] < dist[u])) {
                u = j;
            }
        }
        
        if (u == -1) break;
        visited[u] = true;
        
        // 松弛操作
        for (int v = 0; v < n; ++v) {
            if (dist[u] + g[u][v] < dist[v]) {
                dist[v] = dist[u] + g[u][v];
            }
        }
    }
    
    return dist[n-1] == INF ? -1 : dist[n-1];
}

int main() {
    int n, m;
    cin >> n >> m;
    
    vector<vector<int>> g(n, vector<int>(n, INF));
    for (int i = 0; i < n; ++i) {
        g[i][i] = 0;
    }
    
    for (int i = 0; i < m; ++i) {
        int x, y, z;
        cin >> x >> y >> z;
        g[x-1][y-1] = min(g[x-1][y-1], z);
    }
    
    cout << dijkstra(g) << endl;
    
    return 0;
}
