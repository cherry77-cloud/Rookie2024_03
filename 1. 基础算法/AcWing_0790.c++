#include <bits/stdc++.h>
using namespace std;

const double eps = 1e-8;

int main() 
{
    double n;
    scanf("%lf", &n);

    auto binary_search = [n](double l, double r) -> double {
        while (l + eps < r) {
            double mid = (l + r) / 2;
            if (mid * mid * mid > n) {
                r = mid;
            } else {
                l = mid;
            }
        }
        return l;
    };

    double result = binary_search(-100, 100);
    printf("%.6lf\n", result);

    return 0;
}
