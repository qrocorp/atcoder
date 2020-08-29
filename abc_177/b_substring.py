def main():
    s = input()
    t = input()

    # sがtの長さにおいて一致している最大の文字数を特定
    max_counter = 0

    for i in range(len(s)-len(t)+1):
        counter = 0
        for j in range(len(t)):
            if s[i+j] == t[j]:
                counter += 1
        if counter > max_counter:
            max_counter = counter

    answer = len(t) - max_counter
    print(answer)


if __name__ == "__main__":
    main()
