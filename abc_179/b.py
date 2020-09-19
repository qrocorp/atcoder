def main():
    n = int(input())

    count = 0
    answer = 'No'
    for i in range(n):
        d = list(map(int, input().split()))
        if d[0] == d[1]:
            count += 1
        else:
            count = 0
        if count >= 3:
            answer = 'Yes'

    print(answer)


if __name__ == '__main__':
    main()
