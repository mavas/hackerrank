import fileinput


def main():
    score = 0

    with fileinput.input() as fh:
        N = int(fh.readline().strip())
        print(N)

        compartments = [] * N
        for i in range(N):
            a, b = fh.readline().strip().split(" ")
            compartments.append((int(a), int(b)))
        print(compartments)


if __name__ == '__main__':
    main()
