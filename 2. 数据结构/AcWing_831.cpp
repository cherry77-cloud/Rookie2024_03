#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> kmp(const string& query, const string& pattern) 
{
    int n = query.size();
    int m = pattern.size();
    vector<int> result;

    // 1. 计算模式串 pattern 的前缀函数 fail
    vector<int> fail(m, -1);
    for (int i = 1; i < m; ++i) {
        int j = fail[i - 1];
        while (j != -1 && pattern[j + 1] != pattern[i]) {
            j = fail[j];
        }
        if (pattern[j + 1] == pattern[i]) {
            fail[i] = j + 1;
        }
    }

    // 2. 在字符串 query 中查找模式串 pattern
    int match = -1;
    for (int i = 0; i < n; ++i) {
        while (match != -1 && pattern[match + 1] != query[i]) {
            match = fail[match];
        }
        if (pattern[match + 1] == query[i]) {
            ++match;
        }
        if (match == m - 1) {
            result.push_back(i - m + 1);
            match = fail[match];
        }
    }

    return result;
}

int main() 
{
    int N, M;
    string pattern, query;
    cin >> N >> pattern >> M >> query;
    vector<int> result = kmp(query, pattern);
    for (int i = 0; i < result.size(); ++i) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}
