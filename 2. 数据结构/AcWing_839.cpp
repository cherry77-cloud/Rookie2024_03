#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

class IndexedMinHeap {
private:
    static const int N = 100010;
    int heap[N];
    int ph[N];
    int hp[N];
    int tot;
    int kth;

    void heap_swap(int a, int b) {
        swap(heap[a], heap[b]);
        swap(hp[a], hp[b]);
        swap(ph[hp[a]], ph[hp[b]]);
    }

    void up(int p) {
        while (p / 2 && heap[p] < heap[p / 2]) {
            heap_swap(p, p / 2);
            p /= 2;
        }
    }

    void down(int u) {
        int rt = u;
        if (u * 2 <= tot && heap[u * 2] < heap[rt]) rt = u * 2;
        if (u * 2 + 1 <= tot && heap[u * 2 + 1] < heap[rt]) rt = u * 2 + 1;
        if (rt != u) {
            heap_swap(rt, u);
            down(rt);
        }
    }

public:
    IndexedMinHeap() : tot(0), kth(0) {}

    void insert(int x) {
        tot++; kth++;
        heap[tot] = x;
        hp[tot] = kth;
        ph[kth] = tot;
        up(tot);
    }

    int getMin() {
        return heap[1];
    }

    void deleteMin() {
        heap_swap(1, tot);
        tot--;
        down(1);
    }

    void deleteKth(int k) {
        int pos = ph[k];
        heap_swap(pos, tot);
        tot--;
        up(pos);
        down(pos);
    }

    void updateKth(int k, int x) {
        int pos = ph[k];
        heap[pos] = x;
        up(pos); 
        down(pos);
    }

    bool isEmpty() const {
        return tot == 0;
    }

    int size() const {
        return tot;
    }
};

int main() {
    IndexedMinHeap heap;
    int n;
    cin >> n;

    while (n--) {
        string op;
        cin >> op;

        if (op == "I") {
            int x;
            cin >> x;
            heap.insert(x);
        } else if (op == "PM") {
            cout << heap.getMin() << endl;
        } else if (op == "DM") {
            heap.deleteMin();
        } else if (op == "D") {
            int k;
            cin >> k;
            heap.deleteKth(k);
        } else if (op == "C") {
            int k, x;
            cin >> k >> x;
            heap.updateKth(k, x);
        }
    }

    return 0;
}
