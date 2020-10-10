def main():
    n, s = input().split()
    n = int(n)
    l = list()
    for i in range(n):
        if s[i] == 'A':
            l.append(1)
        elif s[i] == 'T':
            l.append(-1)
        elif s[i] == 'C':
            l.append(10000)
        elif s[i] == 'G':
            l.append(-10000)

    count = 0

    for i in range(n):
        sum_l = 0
        for j in range(i, n):
            sum_l += l[j]
            if sum_l == 0:
                count += 1
    print(count)


if __name__ == '__main__':
    main()

'''
    char_len = 2
    while True:
        for i in range(n - char_len+1):
            if sum(l[i:i+char_len]) == 0:
                count += 1
        char_len += 2
        if char_len > n:
            break
'''


'''
    char_len = 1
    flag = 0
    while True:
        for i in range(n):  # i は部分文字列の位置
            for j in range(n):  # j は照合する文字列の位置
                for k in range(char_len + 1):  # k は文字列比較のため位置文字ずつ走査
                    if i+k >= n or j+k >= n:
                        break
                    if (s[i+k] == 'A' and s[j+k] == 'T') or (s[i+k] == 'T' and s[j+k] == 'A') or (s[i+k] == 'C' and s[j+k] == 'G') or (s[i+k] == 'G' and s[j+k] == 'C'):
                        if k == char_len:
                            flag = 1
                            break
                        else:
                            continue
                    else:
                        break
                if flag == 1:
                    count += 1
                    break
            flag = 0
        char_len += 1
        if char_len > n - 1:
            break

    print(count)
'''
'''
その文字列を並べ替えると相補的な文字列が存在する、部分文字列の個数を求める
A <-> T
C <-> G

2文字 ... n-1文字

AとTの個数
CとGの個数
が同じだと成立


'''
