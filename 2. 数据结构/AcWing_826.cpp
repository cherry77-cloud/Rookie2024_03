#include <iostream>
#include <vector>

using namespace std;

class Node {
public:
    int val;
    Node* next;
    Node(int val) : val(val), next(nullptr) {}
};

class LinkedList {
private:
    Node* head;
    vector<Node*> inserted;

public:
    LinkedList() : head(nullptr) {
        inserted.push_back(nullptr); // inserted[0] 占位，无效
    }

    void insert_head(int x) {
        Node* newNode = new Node(x);
        newNode->next = head;
        head = newNode;
        inserted.push_back(newNode); // 记录插入顺序
    }

    void remove_after_k(int k) {
        if (k == 0) {
            Node* temp = head;
            head = head->next;
            delete temp;
        } else {
            Node* prev = inserted[k];
            if (prev->next) {
                Node* temp = prev->next;
                prev->next = temp->next;
                delete temp;
            }
        }
    }

    void insert_after_k(int k, int x) {
        Node* prev = inserted[k];
        Node* newNode = new Node(x);
        newNode->next = prev->next;
        prev->next = newNode;
        inserted.push_back(newNode);
    }

    void print() {
        Node* curr = head;
        while (curr) {
            cout << curr->val << " ";
            curr = curr->next;
        }
        cout << endl;
    }
};

int main() {
    int M;
    cin >> M;

    LinkedList lst;

    while (M--) {
        char op;
        cin >> op;

        if (op == 'H') {
            int x;
            cin >> x;
            lst.insert_head(x);
        } else if (op == 'D') {
            int k;
            cin >> k;
            lst.remove_after_k(k);
        } else if (op == 'I') {
            int k, x;
            cin >> k >> x;
            lst.insert_after_k(k, x);
        }
    }

    lst.print();
    return 0;
}
