#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

int multiple_knapsack(const vector<int>& volumes, const vector<int>& weights, const vector<int>& counts, int capacity) {
    vector<int> dp(capacity + 1, 0);

    for (int i = 0; i < volumes.size(); ++i) {
        int v = volumes[i], w = weights[i], c = counts[i];
        
        // 对每个余数类单独处理
        for (int mod = 0; mod < v; ++mod) {
            deque<pair<int, int>> q; // 单调队列 {位置, 值}
            
            // 处理当前余数类的所有可能容量
            for (int k = 0; k * v + mod <= capacity; ++k) {
                int j = k * v + mod; // 实际容量
                int val = dp[j] - k * w; // 剔除k个物品的价值
                
                // 维护队列单调性
                while (!q.empty() && q.back().second <= val) q.pop_back();
                q.emplace_back(k, val);
                
                // 移除过期元素 (超过最大数量限制)
                while (q.front().first < k - c) q.pop_front();
                
                // 更新DP值
                dp[j] = max(dp[j], q.front().second + k * w);
            }
        }
    }
    return dp[capacity];
}

int main() {
    int n, capacity;
    cin >> n >> capacity;

    vector<int> volumes(n), weights(n), counts(n);
    for (int i = 0; i < n; ++i) {
        cin >> volumes[i] >> weights[i] >> counts[i];
    }

    int ans = multiple_knapsack(volumes, weights, counts, capacity);
    cout << ans << endl;
    return 0;
}
