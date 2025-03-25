#include <iostream>
#include <vector>
#include <functional>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<vector<int>> result;
    vector<int> path;
    vector<bool> visited(n, false);
    
    function<void(int)> dfs = [&](int u) {
        if (u == n) {
            result.push_back(path);
            return;
        }
        
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                visited[i] = true;
                path.push_back(i + 1);
                dfs(u + 1);
                path.pop_back();
                visited[i] = false;
            }
        }
    };
    
    dfs(0);
    
    // 输出结果
    for (const auto& perm : result) {
        for (int num : perm) {
            cout << num << " ";
        }
        cout << "\n";
    }
    
    return 0;
}
