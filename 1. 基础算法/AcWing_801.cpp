#include <iostream>
#include <vector>

using namespace std;

int main() 
{
    int n;
    std::cin >> n;
    std::vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }

    auto hamming_weight1 = [](int x) -> int {
        int ret = 0;
        while (x) {
            ret++;
            x = x & (x - 1);
        }
        return ret;
    };

    auto hamming_weight2 = [](int x) -> int {
        int ret = 0;
        while (x) {
            ret++;
            x -= x & -x;
        }
        return ret;
    };

    // for (int num : nums) {
    //     std::cout << hamming_weight1(num) << " ";
    // }
    // std::cout << std::endl;

    for (int num : nums) {
        std::cout << hamming_weight2(num) << " ";
    }
    std::cout << std::endl;

    return 0;
}
