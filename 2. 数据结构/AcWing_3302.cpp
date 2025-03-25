#include <iostream>
#include <cstring>
#include <algorithm>
#include <stack>
#include <unordered_map>

using namespace std;

stack<int> num;   // 数字栈    
stack<char> op;   // 运算符栈

void eval() {  // 模拟表达式二叉树子树的运算      
    auto b = num.top(); num.pop();  // b是右孩子节点
    auto a = num.top(); num.pop();  // a是左孩子节点
    auto c = op.top(); op.pop();    // c是父亲节点
    int x = 0;
    if (c == '+')  x = a + b;
    if (c == '-')  x = a - b;
    if (c == '*')  x = a * b;
    if (c == '/')  x = a / b;
    num.push(x);
}

int main() {
    
    unordered_map<char, int> pr{{'+', 1}, {'-', 1}, {'*', 2}, {'/', 2}};
    
    string str;  cin >> str;
    
    for (int i = 0; i < str.size(); ++i) {
        auto c = str[i];
        
        if (isdigit(c)) { // 模拟取出数字的过程
            int x = 0, j = i;
            while (j < str.size() && isdigit(str[j])) {
                x = x * 10 + str[j] - '0';
                j++;
            }
            i = j - 1;
            num.push(x);
        }
        
        else if (c == '(') op.push(c); // 如果是左括号，压入栈中
        
        else if (c == ')') { // 如果是右括号，就算出左括号至右括号之间的表达式子树
            while (op.top() != '(')  eval();
            op.pop(); // 弹出左括号
        }
        
        else {
            // 某棵子树没有被遍历完，比如 pr[op.top()] = *, pr[c] = +, 就要先算乘法
            while (op.size() && op.top() != '(' && pr[op.top()] >= pr[c])  eval();
            op.push(c); // 将其它运算符入栈
        }
    }
    
    while (op.size())  eval();
    
    cout << num.top() << endl;
    
    return 0;
}
