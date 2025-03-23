#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

const int N = 300010;
typedef pair<int, int> PII;

int a[N], s[N];

vector<int> all;
vector<PII> add, query;

int find(int x) 
{
    return lower_bound(all.begin(), all.end(), x) - all.begin();
}


int main() {
    
    int n, m;  cin >> n >> m;
    
    while (n--) {
        int x, c; cin >> x >> c;
        all.push_back(x);
        add.push_back({x, c});
    }
    
    while (m--) {
        int l, r;  cin >> l >> r;
        all.push_back(l);
        all.push_back(r);
        query.push_back({l, r});
    }
    
    sort(all.begin(), all.end());
    all.erase(unique(all.begin(), all.end()), all.end());
    
    for (auto item : add) {
        int x = find(item.first);
        a[x] += item.second;
    }
    
    for (int i = 0; i < all.size(); ++i) s[i + 1] = s[i] + a[i];
    
    for (auto item : query) {
        int l = find(item.first), r = find(item.second);
        cout << s[r + 1] - s[l] << endl;
    }
    
    return 0;
}
