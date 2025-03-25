#include <iostream>
#include <vector>
#include <climits>

using namespace std;

const int INF = 0x3f3f3f3f;

void floydWarshall(vector<vector<int>>& dist) {
    int n = dist.size();
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (dist[i][k] != INF && dist[k][j] != INF) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
}

int main() {
    int n, m, Q;
    cin >> n >> m >> Q;

    vector<vector<int>> dist(n, vector<int>(n, INF));
    for (int i = 0; i < n; ++i) dist[i][i] = 0;

    for (int i = 0; i < m; ++i) {
        int x, y, z;
        cin >> x >> y >> z;
        dist[x-1][y-1] = min(dist[x-1][y-1], z); // 转换为0-based
    }

    floydWarshall(dist);

    while (Q--) {
        int x, y;
        cin >> x >> y;
        x--; y--; // 转换为0-based
        if (dist[x][y] > INF / 2) {
            cout << "impossible" << endl;
        } else {
            cout << dist[x][y] << endl;
        }
    }

    return 0;
}
