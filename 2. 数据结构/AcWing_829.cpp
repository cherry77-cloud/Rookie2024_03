#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main() {
    deque<int> q;  // 使用 deque 模拟队列
    
    int n;
    cin >> n;
    
    while (n--) {
        string op;
        cin >> op;
        
        if (op == "push") {
            int x;
            cin >> x;
            q.push_back(x);  // 队尾插入
        }
        else if (op == "pop") {
            q.pop_front();  // 队头弹出
        }
        else if (op == "query") {
            cout << q.front() << endl;  // 查询队头
        }
        else {  // empty
            if (q.empty()) {
                cout << "YES" << endl;  // 队列为空
            }
            else {
                cout << "NO" << endl;   // 队列非空
            }
        }
    }
    
    return 0;
}
