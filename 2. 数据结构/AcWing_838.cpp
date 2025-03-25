#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class MinHeap {
private:
    vector<int> heap;
    int heapSize;

    void heapSwap(int a, int b) {
        swap(heap[a], heap[b]);
    }

    void heapifyUp(int p) {
        while (p > 1 && heap[p] < heap[p / 2]) {
            heapSwap(p, p / 2);
            p /= 2;
        }
    }

    void heapifyDown(int u) {
        int smallest = u;
        if (u * 2 <= heapSize && heap[u * 2] < heap[smallest]) smallest = u * 2;
        if (u * 2 + 1 <= heapSize && heap[u * 2 + 1] < heap[smallest]) smallest = u * 2 + 1;
        if (smallest != u) {
            heapSwap(u, smallest);
            heapifyDown(smallest);
        }
    }

public:
    MinHeap() {
        heap.push_back(0);
        heapSize = 0;
    }

    void push(int value) {
        heap.push_back(value);
        heapSize++;
        heapifyUp(heapSize);
    }

    void pop() {
        heapSwap(1, heapSize);
        heap.pop_back();
        heapSize--;
        if (heapSize > 0) heapifyDown(1);
    }

    int top() const { return heap[1]; }
    bool empty() const { return heapSize == 0; }
    size_t size() const { return heapSize; }
};

int main() {
    int n, m;
    cin >> n >> m;

    MinHeap heap;

    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        heap.push(x);
    }

    for (int i = 0; i < m; ++i) {
        cout << heap.top() << " ";
        heap.pop();
    }

    return 0;
}
