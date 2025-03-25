#include <iostream>
#include <vector>
using namespace std;

struct TrieNode {
    TrieNode* children[2] = {nullptr, nullptr};
};

class BinaryTrie {
private:
    TrieNode* root;

public:
    BinaryTrie() { root = new TrieNode(); }

    void insert(int num) {
        TrieNode* p = root;
        for (int i = 30; i >= 0; --i) {
            int bit = (num >> i) & 1;
            if (!p->children[bit]) {
                p->children[bit] = new TrieNode();
            }
            p = p->children[bit];
        }
    }

    int queryMaxXOR(int num) {
        TrieNode* p = root;
        int res = 0;
        for (int i = 30; i >= 0; --i) {
            int bit = (num >> i) & 1;
            int toggle = 1 - bit;
            
            if (p->children[toggle]) {
                res |= (1 << i);
                p = p->children[toggle];
            } else {
                p = p->children[bit];
            }
        }
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    cin >> N;
    vector<int> nums(N);
    for (int i = 0; i < N; ++i) {
        cin >> nums[i];
    }
    
    BinaryTrie trie;
    int max_xor = 0;
    
    // 先插入第一个数
    if (N > 0) {
        trie.insert(nums[0]);
    }
    
    // 从第二个数开始查询
    for (int i = 1; i < N; ++i) {
        max_xor = max(max_xor, trie.queryMaxXOR(nums[i]));
        trie.insert(nums[i]);
    }
    
    cout << max_xor << endl;
    return 0;
}
