#include <iostream>
#include <vector>
#include <stack>

using namespace std;

vector<int> leftFirstSmaller1(const vector<int>& nums) {
    int n = nums.size();
    vector<int> res(n, -1);
    stack<int> st;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && nums[st.top()] >= nums[i]) {
            st.pop();
        }
        if (!st.empty()) {
            res[i] = nums[st.top()];
        }
        st.push(i);
    }

    return res;
}

vector<int> leftFirstSmaller2(const vector<int>& nums) {
    int n = nums.size();
    vector<int> res(n, -1);
    stack<int> st;

    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && nums[st.top()] > nums[i]) {
            res[st.top()] = nums[i];
            st.pop();
        }
        st.push(i);
    }
    return res;
}

int main() {
    int N;
    cin >> N;
    vector<int> nums(N);
    for (int i = 0; i < N; ++i) {
        cin >> nums[i];
    }

    vector<int> result = leftFirstSmaller2(nums);
    for (int x : result) {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}
