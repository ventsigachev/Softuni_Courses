def tri_count(b):
    if b == 1 or b == 2:
        return 1
    elif b == 3:
        return 2
    else:
        return (tri_count(b - 1) +
                tri_count(b - 2) +
                tri_count(b - 3))


def print_tri_count(a):
    for i in range(1, a + 1):
        print(tri_count(i), end=' ')


def main():
    num = int(input())
    print_tri_count(num)


if __name__ == "__main__":
    main()
