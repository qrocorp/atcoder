def main():
    s = input()

    if s[-1] == 's':
        s = s + 'es'
    else:
        s = s + 's'
    print(s)


if __name__ == '__main__':
    main()
