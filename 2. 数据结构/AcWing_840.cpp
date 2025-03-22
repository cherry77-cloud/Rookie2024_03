#include <iostream>
#include <vector>
#include <list>
using namespace std;

class MyHashSet {
private:
    vector<list<int>> data;
    static const int base = 131;
    static int hash(int key) {
        int h = key % base;
        if (h < 0) h += base;
        return h;
    }

public:
    MyHashSet() : data(base) {}
    
    void add(int key) {
        int h = hash(key);
        for (auto it = data[h].begin(); it != data[h].end(); it++) {
            if ((*it) == key) {
                return;
            }
        }
        data[h].push_back(key);
    }
    
    void remove(int key) {
        int h = hash(key);
        for (auto it = data[h].begin(); it != data[h].end();) {
            if ((*it) == key) {
                it = data[h].erase(it);
            } else {
                ++it;
            }
        }
    }
    
    bool contains(int key) {
        int h = hash(key);
        for (auto it = data[h].begin(); it != data[h].end(); it++) {
            if ((*it) == key) {
                return true;
            }
        }
        return false;
    }
};

int main() 
{
    int n;
    cin >> n;
    
    MyHashSet hashSet;
    
    while (n--) {
        char op;
        int x;
        cin >> op >> x;
        if (op == 'I') {
            hashSet.add(x);
        } else if (op == 'Q') {
            if (hashSet.contains(x)) {
                cout << "Yes" << endl;
            } else {
                cout << "No" << endl;
            }
        }
    }
    
    return 0;
}
