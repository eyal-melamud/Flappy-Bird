def t1():
    a = [[j + i * 3 + 1 for j in range(3)] for i in range(4)]
    print(a)
    b = [[], [], []]
    for i in range(4):
        for j in range(3):
            pass


def main():
    a = list(range(1, 13))  # 4*3
    b = [0 for i in range(12)]  # 3*4
    for i in range(4):
        for j in range(3):
            b[j * 4 + i] = a[i * 3 + j]
    print(a)
    print(b)


if __name__ == '__main__':
    main()
