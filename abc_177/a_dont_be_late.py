def main():
    x = [int(_) for _ in input().split()]
    d = x[0]
    t = x[1]
    s = x[2]

    if t * s >= d:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
