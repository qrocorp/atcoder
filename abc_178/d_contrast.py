def rec(a, n):  # 項の数と剰余値
    if a == 1:
        return 1
    if a == 2:
        return n + 1
    for i in range(n):
        v += rec(a-1, i)
    return v


def main():
    s = int(input())

    mod = 10**9 + 7


if __name__ == "__main__":
    main()

'''
すべての項が3以上の整数
その総和がSである数列がいくつあるか

項が３つの場合
'''


def recursive(n):
    if n < 1:
        return n
    return n + recursive(recursive(n-1))
