#include <iostream>
#include <cstring>
#include <queue>
#include <algorithm>

using namespace std;

typedef pair<int, int> PII;

const int N = 110;

int n, m;
int g[N][N], dist[N][N];
queue<PII> que;

int bfs() {
    
    int dx[4] = {0, 0, -1, 1}, dy[4] = {-1, 1, 0, 0};
    memset(dist, -1, sizeof(dist));
    dist[0][0] = 0;
    que.push({0, 0});
    while (!que.empty()) {
        auto t = que.front();
        que.pop();
        for (int i = 0; i < 4; ++i) {
            int tx = t.first + dx[i];
            int ty = t.second + dy[i];
            if (tx >= 0 && tx < n && ty >= 0 && ty < m && g[tx][ty] == 0 && dist[tx][ty] == -1) {
                dist[tx][ty] = dist[t.first][t.second] + 1;
                que.push({tx, ty});
            }
        }
    }
    
    return dist[n - 1][m - 1];
}

int main() {
    
    cin >> n >> m;
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> g[i][j];
        }
    }
    
    cout << bfs() << endl;
    
    return 0;
}
