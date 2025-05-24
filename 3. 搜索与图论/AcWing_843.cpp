#include <iostream>
using namespace std;
const int N = 10;

int n;
bool col[N], dg[N * 2], udg[N * 2];
char g[N][N];

void dfs(int row) 
{
    if (row == n) {
        for (int i = 0; i < n; ++i)  puts(g[i]);
        puts("");
        return;
    }
    
    for (int i = 0; i < n; ++i) {
        if (!col[i] && !dg[i - row + n] && !udg[row + i]) {
            g[row][i] = 'Q';
            col[i] = dg[i - row + n] = udg[row + i] = true;
            dfs(row + 1);
            g[row][i] = '.';
            col[i] = dg[i - row + n] = udg[row + i] = false;
        }
    }
}

int main() 
{
    
    cin >> n;
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            g[i][j] = '.';
        }
    }
    
    dfs(0);
    
    return 0;
}
