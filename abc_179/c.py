def main():
    n = int(input())
    ans = 0
    for a in range(1, n):
        ans += (n-1) // a
    print(ans)


if __name__ == '__main__':
    main()


'''

import math
import sympy


def main():
    n = int(input())

    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 0
    for i in range(2, n+1):
        dp[i] = dp[i-1] + sympy.divisor_count(i-1)

    print(dp[-1])


if __name__ == '__main__':
    main()


def num_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return len(lower_divisors + upper_divisors[::-1])



def factorization(n):
    def factor_sub(n, m):
        c = 0
        while n % m == 0:
            c += 1
            n /= m
        return c, n
    #
    buff = []
    c, m = factor_sub(n, 2)
    if c > 0:
        buff.append((2, c))
    c, m = factor_sub(m, 3)
    if c > 0:
        buff.append((3, c))
    x = 5
    while m >= x * x:
        c, m = factor_sub(m, x)
        if c > 0:
            buff.append((x, c))
        if x % 6 == 5:
            x += 2
        else:
            x += 4
    if m > 1:
        buff.append((m, 1))
    return buff


def divisor_num(n):
    a = 1
    for _, x in factorization(n):
        a *= x + 1
    return a


def num_divisors_trial_division(n):
    num = 0
    for i in range(1, int(math.sqrt(n) + 1e-9) + 1):
        if n % i == 0:
            num += 1
            if n != i**2:
                num += 1

    return num
'''
