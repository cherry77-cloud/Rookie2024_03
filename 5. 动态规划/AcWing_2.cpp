#include <iostream>
#include <vector>
#include <map>
#include <functional>

using namespace std;

int zero_one_knapsack(const vector<int>& volumes, const vector<int>& weights, int capacity) {
    vector<int> dp(capacity + 1, 0);
    
    for (int i = 0; i < volumes.size(); ++i) {
        for (int j = capacity; j >= volumes[i]; --j) {
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

    cout << zero_one_knapsack(volumes, weights, capacity) << endl;
    return 0;
}
