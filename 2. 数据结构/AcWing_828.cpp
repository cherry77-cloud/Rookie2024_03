#include <iostream>
#include <deque>
#include <string>

template <typename T, typename Container = std::deque<T>>
class MyStack {
private:
    Container data;
public:
    bool empty() const {
        return data.empty();
    }

    T top() const {
        return data.back();
    }

    void push(const T& value) {
        data.push_back(value);
    }

    void pop() {
        data.pop_back();
    }
};

int main() 
{
    int M;
    std::cin >> M;
    MyStack<int> stack;

    while (M--) {
        std::string op;
        std::cin >> op;
        if (op == "push") {
            int x;
            std::cin >> x;
            stack.push(x);
        } else if (op == "pop") {
            stack.pop();
        } else if (op == "empty") {
            std::cout << (stack.empty() ? "YES" : "NO") << std::endl;
        } else if (op == "query") {
            std::cout << stack.top() << std::endl;
        }
    }

    return 0;
}
