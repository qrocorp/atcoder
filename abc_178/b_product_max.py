def main():
    a, b, c, d = map(int, input().split())
    # a, c が両方マイナスの場合, acとbdで比較
    print(max(a*c, b*d, a*d, b*c))


if __name__ == "__main__":
    main()
