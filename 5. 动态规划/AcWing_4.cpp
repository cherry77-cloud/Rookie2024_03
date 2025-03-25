#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

int multiple_knapsack(const vector<int>& volumes, const vector<int>& weights, const vector<int>& counts, int capacity) {
    vector<pair<int, int>> items; // {体积, 价值}

    for (int i = 0; i < volumes.size(); ++i) {
        int k = 1;
        int remaining = counts[i];
        while (k <= remaining) {
            items.emplace_back(volumes[i] * k, weights[i] * k);
            remaining -= k;
            k *= 2;
        }
        if (remaining > 0) {
            items.emplace_back(volumes[i] * remaining, weights[i] * remaining);
        }
    }

    vector<int> dp(capacity + 1, 0);
    for (const auto& [v, w] : items) {
        for (int j = capacity; j >= v; --j) {
            dp[j] = max(dp[j], dp[j - v] + w);
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
