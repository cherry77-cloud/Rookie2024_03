#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


string addHighPrecision(const string& s1, const string& s2) 
{
    vector<int> num1, num2;

    // 将字符串转换为数字（逆序存储）
    for (int i = s1.length() - 1; i >= 0; i--) num1.push_back(s1[i] - '0');
    for (int i = s2.length() - 1; i >= 0; i--) num2.push_back(s2[i] - '0');

    vector<int> result;
    int carry = 0;

    // 逐位相加
    for (int i = 0; i < num1.size() || i < num2.size() || carry; i++) {
        int val1 = (i < num1.size()) ? num1[i] : 0;
        int val2 = (i < num2.size()) ? num2[i] : 0;
        int sum = val1 + val2 + carry;
        result.push_back(sum % 10);
        carry = sum / 10;
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
    cout << addHighPrecision(s1, s2) << endl;
    return 0;
}
