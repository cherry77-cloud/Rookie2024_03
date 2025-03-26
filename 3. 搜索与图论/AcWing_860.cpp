#include <iostream>
#include <vector>
#include <queue>

using namespace std;

bool isBipartite(const vector<vector<int>>& adj) {
    int n = adj.size();
    vector<int> color(n, 0); // 0:未染色, 1:红色, 2:蓝色
    queue<int> q;

    for (int i = 0; i < n; ++i) {
        if (color[i] != 0) continue;
        
        q.push(i);
        color[i] = 1;
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            for (int v : adj[u]) {
                if (color[v] == 0) {
                    color[v] = 3 - color[u]; // 交替染色
                    q.push(v);
                } 
                else if (color[v] == color[u]) {
                    return false; // 发现冲突直接返回
                }
            }
        }
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    vector<vector<int>> adj(n);
    
    // 构建邻接表（0-based）
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        if (u == v) { // 自环直接判定非二分图
            cout << "No";
            return 0;
        }
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    cout << (isBipartite(adj) ? "Yes" : "No");
    return 0;
}
