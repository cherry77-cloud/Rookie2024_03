#include <iostream>
#include <vector>
#include <stdexcept>
#include <algorithm>

using namespace std;

class MinHeap {
private:
    vector<int> heap;

    void heapifyUp(int p) {
        while (p > 0 && heap[p] < heap[(p - 1) / 2]) {
            std::swap(heap[p], heap[(p - 1) / 2]);
            p = (p - 1) / 2;
        }
    }

    void heapifyDown(int u) {
        int size = heap.size();
        while (true) {
            int left = 2 * u + 1, right = 2 * u + 2, smallest = u;
            if (left < size && heap[left] < heap[smallest]) smallest = left;
            if (right < size && heap[right] < heap[smallest]) smallest = right;
            if (smallest == u) break;
            swap(heap[u], heap[smallest]);
            u = smallest;
        }
    }

public:
    void push(int value) {
        heap.push_back(value);
        heapifyUp(heap.size() - 1);
    }

    void pop() {
        heap[0] = heap.back();
        heap.pop_back();
        if (!heap.empty()) heapifyDown(0);
    }

    int top() const {
        return heap[0];
    }

    bool empty() const { return heap.empty(); }
    size_t size() const { return heap.size(); }
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
