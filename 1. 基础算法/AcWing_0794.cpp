#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// 高精度除法（返回商和余数）
pair<string, long long> divideHighPrecision(const string& dividend, long long divisor) 
{
    long long remainder = 0;  // 余数
    string quotient;          // 商

    // 逐位处理被除数（从高位到低位）
    for (char c : dividend) {
        remainder = remainder * 10 + (c - '0');  // 更新余数
        quotient.push_back(remainder / divisor + '0');  // 计算当前位的商
        remainder %= divisor;  // 更新余数
    }

    // 去除商的前导零
    quotient.erase(0, quotient.find_first_not_of('0'));
    if (quotient.empty()) quotient = "0";  // 商为0的情况

    return {quotient, remainder};
}

int main() 
{
    string dividend;
    long long divisor;
    cin >> dividend >> divisor;

    auto result = divideHighPrecision(dividend, divisor);
    cout << result.first << endl;
    cout << result.second << endl;

    return 0;
}
