#include <iostream>
#include <vector>
using namespace std;

class UnionFind {
private:
    vector<int> fa;

public:
    UnionFind(int n) {
        fa.resize(n + 1);
        for (int i = 1; i <= n; ++i) {
            fa[i] = i;
        }
    }

    int find(int x) {
        int root = x;
        while (fa[root] != root)
            root = fa[root];

        while (x != root) {
            int parent = fa[x];
            fa[x] = root;
            x = parent;
        }
        return root;
    }

    void merge(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        if (rootA != rootB) {
            fa[rootA] = rootB;
        }
    }

    bool isConnected(int a, int b) {
        return find(a) == find(b);
    }
};

int main() {
    int n, m;
    cin >> n >> m;

    UnionFind uf(n); // 初始化并查集

    while (m--) {
        char op;
        int a, b;
        cin >> op >> a >> b;

        if (op == 'M') {
            uf.merge(a, b); // 合并操作
        } else {
            cout << (uf.isConnected(a, b) ? "Yes" : "No") << endl; // 查询操作
        }
    }

    return 0;
}
