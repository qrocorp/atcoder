def main():
    n = int(input())

    mod = 10**9 + 7

    # すべての組み合わせから、いずれかの条件を満たさないパターンを引く

    pattern = 10 ** n
    not_pattern = (9 ** n) + (9 ** n) - (8 ** n)

    answer = (pattern - not_pattern) % mod

    print(answer)


if __name__ == "__main__":
    main()
