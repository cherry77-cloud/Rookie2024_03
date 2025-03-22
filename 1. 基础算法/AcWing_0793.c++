#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// 高精度乘法
string multiplyHighPrecision(const string& s1, const string& s2) 
{
    const int BASE = 1e9;  // 压 9 位

    // 将字符串按每 9 位分割成数字
    auto split = [](const string& s, vector<int>& nums) {
        for (int i = s.length(); i > 0; i -= 9)
            nums.push_back(stoi(s.substr(max(0, i - 9), i - max(0, i - 9))));
    };

    vector<int> num1, num2;
    split(s1, num1);
    split(s2, num2);

    // 结果数组
    vector<long long> result(num1.size() + num2.size(), 0);

    // 逐块相乘
    for (int i = 0; i < num1.size(); i++) {
        for (int j = 0; j < num2.size(); j++) {
            long long product = (long long)num1[i] * num2[j];
            result[i + j] += product;
            result[i + j + 1] += result[i + j] / BASE;
            result[i + j] %= BASE;
        }
    }

    // 处理进位
    for (int i = 0; i < result.size() - 1; i++) {
        result[i + 1] += result[i] / BASE;
        result[i] %= BASE;
    }

    // 去除前导零
    while (result.size() > 1 && result.back() == 0)
        result.pop_back();

    // 将结果转换为字符串
    string resultStr;
    for (int i = result.size() - 1; i >= 0; i--) {
        if (i == result.size() - 1) {
            resultStr += to_string(result[i]);
        } else {
            char buffer[10];
            snprintf(buffer, sizeof(buffer), "%09lld", result[i]);
            resultStr += buffer;
        }
    }

    return resultStr;
}

int main() 
{
    string s1, s2;
    cin >> s1 >> s2;
    cout << multiplyHighPrecision(s1, s2) << endl;
    return 0;
}
