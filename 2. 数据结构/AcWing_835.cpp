#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Trie {
private:
    vector<Trie*> children;
    bool isEnd;
    unordered_map<string, int> countMap;

public:
    Trie() : children(26), isEnd(false) {}
    
    void insert(string word) {
        Trie* node = this;
        for (char ch : word) {
            ch -= 'a';
            if (node->children[ch] == nullptr) {
                node->children[ch] = new Trie();
            }
            node = node->children[ch];
        }
        node->isEnd = true;
        countMap[word]++; // 在哈希表中增加计数
    }
    
    bool search(string word) {
        Trie* node = this;
        for (char ch : word) {
            ch -= 'a';
            if (node->children[ch] == nullptr) {
                return false;
            }
            node = node->children[ch];
        }
        return node->isEnd;
    }
    
    bool startsWith(string prefix) {
        Trie* node = this;
        for (char ch : prefix) {
            ch -= 'a';
            if (node->children[ch] == nullptr) {
                return false;
            }
            node = node->children[ch];
        }
        return true;
    }
    
    // 添加的新方法：查询字符串出现次数
    int getCount(string word) {
        return countMap[word];
    }
};

int main() {
    int N;
    cin >> N;
    
    Trie trie;
    
    while (N--) {
        char op;
        string x;
        cin >> op >> x;
        
        if (op == 'I') {
            trie.insert(x);
        } else if (op == 'Q') {
            cout << trie.getCount(x) << endl;
        }
    }
    
    return 0;
}
