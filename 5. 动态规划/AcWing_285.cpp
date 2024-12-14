#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
const int N = 6001;

vector<int> children[N];
int happy[N];
int dp[N][2];
bool has_parent[N];

void dfs(int u) 
{
    dp[u][1] = happy[u];
    dp[u][0] = 0;
    for (int v : children[u]) {
        dfs(v);
        dp[u][1] += dp[v][0];
        dp[u][0] += max(dp[v][0], dp[v][1]);
    }
}

int main() 
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> happy[i];
    
    for (int i = 1; i < n; i++) {
        int l, k;
        cin >> l >> k;
        children[k].push_back(l);
        has_parent[l] = true;  // 标记 l 有父节点
    }

    int root = 1;  // 找到根节点，即没有父节点的节点
    while (has_parent[root]) {
        root += 1;
    }

    dfs(root);
    cout << max(dp[root][0], dp[root][1]) << endl;
    return 0;
}
