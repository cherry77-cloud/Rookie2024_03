#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string subtractHighPrecision(const string& s1, const string& s2) 
{
    // 比较两个大整数的大小
    auto isGreaterOrEqual = [](const string& a, const string& b) {
        if (a.length() != b.length()) return a.length() > b.length();
        return a >= b;
    };

    // 如果 s1 < s2，返回负数结果
    if (!isGreaterOrEqual(s1, s2)) return "-" + subtractHighPrecision(s2, s1);

    vector<int> num1, num2;

    // 将字符串转换为数字（逆序存储）
    for (int i = s1.length() - 1; i >= 0; i--) num1.push_back(s1[i] - '0');
    for (int i = s2.length() - 1; i >= 0; i--) num2.push_back(s2[i] - '0');

    vector<int> result;
    int borrow = 0;

    // 逐位相减
    for (int i = 0; i < num1.size(); i++) {
        int val1 = num1[i] - borrow;
        int val2 = (i < num2.size()) ? num2[i] : 0;
        borrow = 0;

        if (val1 < val2) {
            val1 += 10;
            borrow = 1;
        }

        result.push_back(val1 - val2);
    }

    // 去除前导零
    while (result.size() > 1 && result.back() == 0) result.pop_back();

    // 将结果转换为字符串
    string resultStr;
    for (int i = result.size() - 1; i >= 0; i--) resultStr += to_string(result[i]);

    return resultStr;
}


int main() 
{
    string s1, s2;
    cin >> s1 >> s2;
    cout << subtractHighPrecision(s1, s2) << endl;
    return 0;
}
