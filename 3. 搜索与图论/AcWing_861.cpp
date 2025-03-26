#include <iostream>
#include <vector>
#include <functional>
using namespace std;

int hungarian(const vector<vector<int>>& graph, int n_left, int n_right) {
    vector<int> right_match(n_right, -1);
    int result = 0;

    for (int u = 0; u < n_left; ++u) {
        vector<bool> vis(n_right, false);

        function<bool(int)> dfs = [&](int u) {
            for (int v : graph[u]) {
                if (!vis[v]) {
                    vis[v] = true;
                    if (right_match[v] == -1 || dfs(right_match[v])) {
                        right_match[v] = u;
                        return true;
                    }
                }
            }
            return false;
        };

        if (dfs(u)) ++result;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int n1, n2, m;
    cin >> n1 >> n2 >> m;

    vector<vector<int>> graph(n1);
    while (m--) {
        int u, v;
        cin >> u >> v;
        graph[u-1].push_back(v-1); // 转换为0-based
    }

    cout << hungarian(graph, n1, n2);
}
