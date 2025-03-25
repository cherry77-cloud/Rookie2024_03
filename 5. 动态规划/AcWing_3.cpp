#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int complete_knapsack(const vector<int>& volumes, const vector<int>& weights, int capacity) {
    vector<int> dp(capacity + 1, 0);
    
    for (int i = 0; i < volumes.size(); ++i) {
        // 正向遍历以支持重复选择
        for (int j = volumes[i]; j <= capacity; ++j) {
            dp[j] = max(dp[j], dp[j - volumes[i]] + weights[i]);
        }
    }
    return dp[capacity];
}

int main() 
{
    int n, capacity;
    cin >> n >> capacity;

    vector<int> volumes(n);
    vector<int> weights(n);

    for (int i = 0; i < n; ++i) {
        cin >> volumes[i] >> weights[i];
    }

    cout << complete_knapsack(volumes, weights, capacity) << endl;
    return 0;
}
