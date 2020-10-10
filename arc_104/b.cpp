#include <iostream>
#include <vector>
#include <string>
#include <numeric>

using namespace std;

int n;
string s;
vector<int> vec;

int main()
{
    cin >> n >> s;

    for (int i = 0; i < n; i++)
    {
        if (s[i] == 'A')
        {
            vec[i] = 1;
        }
        else if (s[i] == 'T')
        {
            vec[i] = -1;
        }
        else if (s[i] == 'C')
        {
            vec[i] = 10000;
        }
        else if (s[i] == 'G')
        {
            vec[i] = -10000;
        }
    }
    int count = 0;
    int char_len = 2;
    while (true)
    {
        for (int i = 0; i < n - char_len + 1; i++)
        {
            if (accumulate(&vec[i], &vec[i + char_len - 1], 0) == 0)
            {
                count++;
            }
        }
        char_len = char_len + 2;
        if (char_len > n)
        {
            break;
        }
    }
    cout << count << endl;
}
