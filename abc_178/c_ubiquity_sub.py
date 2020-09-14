def main():
    n = int(input())
    print(ubiquity(n))


if __name__ == "__main__":
    main()


def ubiquity(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 2

    for i in range(2, n):
        dp[i+1] = dp[i] *

    return dp[n]


'''
def main():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [0] * (n+1)

    for i in range(n):
        dp[i+1] = max(dp[i], dp[i] + a[i])

    print(dp[n])
'''

9 0 x
0 9 x
9 x 0
0 x 9
x 9 0
x 0 9
10 * 6 - 6 = 54
