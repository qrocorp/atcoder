#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<long long> enum_divisors(long long N)
{
    vector<long long> res;
    for (long long i = 1; i * i <= N; ++i)
    {
        if (N % i == 0)
        {
            res.push_back(i);
            // 重複しないならば i の相方である N/i も push
            if (N / i != i)
                res.push_back(N / i);
        }
    }
    // 小さい順に並び替える
    sort(res.begin(), res.end());
    return res;
}

int num_divisors(long long n)
{
    const auto &res = enum_divisors(n);
    return res.size();
}

int main()
{
    int n;
    cin >> n;
    int dp[1000009];
    dp[0] = 0;
    dp[1] = 0;
    for (int i = 2; i < n + 1; i++)
    {
        dp[i] = dp[i - 1] + num_divisors(i - 1);
    }
    cout << dp[n];
    return 0;
}
