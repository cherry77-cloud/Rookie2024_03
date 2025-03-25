#include <iostream>
#include <vector>

using namespace std;

class UnionFind {
private:
    vector<int> fa;
    vector<int> d; // d[x] 表示 x 到父节点的权值（模3）

public:
    UnionFind(int n) {
        fa.resize(n + 1);
        d.resize(n + 1, 0);
        for (int i = 1; i <= n; ++i) fa[i] = i;
    }

    int find(int x) {
        if (fa[x] != x) {
            int root = find(fa[x]);
            d[x] += d[fa[x]];   // 路径压缩时累加权值
            d[x] %= 3;          // 保持模3范围
            fa[x] = root;
        }
        return fa[x];
    }

    // 合并操作，relation 表示 x 和 y 的关系：0-同类，1-x吃y
    bool unite(int x, int y, int relation) {
        int px = find(x), py = find(y);
        if (px == py) return false; // 已属于同一集合
        
        fa[px] = py;
        d[px] = (d[y] - d[x] + relation + 3) % 3; // 关键公式
        return true;
    }

    // 获取 x 和 y 的关系（需确保同一集合）
    int getRelation(int x, int y) {
        return (d[x] - d[y] + 3) % 3;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m, res = 0;
    cin >> n >> m;

    UnionFind uf(n);
    while (m--) {
        int op, x, y;
        cin >> op >> x >> y;

        if (x > n || y > n) { res++; continue; }

        int px = uf.find(x), py = uf.find(y);
        if (op == 1) { // 断言 x 和 y 是同类
            if (px == py && uf.getRelation(x, y) != 0) res++;
            else if (px != py) uf.unite(x, y, 0);
        } else {       // 断言 x 吃 y
            if (px == py && uf.getRelation(x, y) != 1) res++;
            else if (px != py) uf.unite(x, y, 1);
        }
    }

    cout << res << endl;
    return 0;
}
