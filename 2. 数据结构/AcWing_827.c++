#include <iostream>
#include <vector>
using namespace std;

struct Node {
    int val;
    Node* prev;
    Node* next;
    Node(int v) : val(v), prev(nullptr), next(nullptr) {}
};

class DoubleLinkedList {
private:
    Node* head;
    Node* tail;
    vector<Node*> nodes; // 存储所有插入的节点，nodes[0]无效

public:
    DoubleLinkedList() : head(nullptr), tail(nullptr) {
        nodes.push_back(nullptr); // 索引从1开始
    }

    // 最左端插入
    void insertL(int x) {
        Node* newNode = new Node(x);
        if (!head) {
            head = tail = newNode;
        } else {
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
        }
        nodes.push_back(newNode);
    }

    // 最右端插入
    void insertR(int x) {
        Node* newNode = new Node(x);
        if (!tail) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
        nodes.push_back(newNode);
    }

    // 删除第k个节点
    void remove(int k) {
        Node* target = nodes[k];
        if (target->prev) 
            target->prev->next = target->next;
        else 
            head = target->next;
        
        if (target->next) 
            target->next->prev = target->prev;
        else 
            tail = target->prev;
        
        delete target;
    }

    // 在第k个节点左侧插入
    void insertIL(int k, int x) {
        Node* target = nodes[k];
        Node* newNode = new Node(x);
        newNode->prev = target->prev;
        newNode->next = target;
        
        if (target->prev) 
            target->prev->next = newNode;
        else 
            head = newNode;
        
        target->prev = newNode;
        nodes.push_back(newNode);
    }

    // 在第k个节点右侧插入
    void insertIR(int k, int x) {
        Node* target = nodes[k];
        Node* newNode = new Node(x);
        newNode->prev = target;
        newNode->next = target->next;
        
        if (target->next) 
            target->next->prev = newNode;
        else 
            tail = newNode;
        
        target->next = newNode;
        nodes.push_back(newNode);
    }

    // 输出链表
    void print() {
        Node* curr = head;
        while (curr) {
            cout << curr->val << " ";
            curr = curr->next;
        }
    }
};

int main() {
    int M;
    cin >> M;
    DoubleLinkedList dll;

    while (M--) {
        string op;
        cin >> op;
        if (op == "L") {
            int x; cin >> x;
            dll.insertL(x);
        } else if (op == "R") {
            int x; cin >> x;
            dll.insertR(x);
        } else if (op == "D") {
            int k; cin >> k;
            dll.remove(k);
        } else if (op == "IL") {
            int k, x; cin >> k >> x;
            dll.insertIL(k, x);
        } else if (op == "IR") {
            int k, x; cin >> k >> x;
            dll.insertIR(k, x);
        }
    }

    dll.print();
    return 0;
}
