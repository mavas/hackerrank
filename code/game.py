import fileinput
import random


def main():
    score = 0

    with fileinput.input() as fh:
        N = int(fh.readline().strip())

        compartments = [] * N
        for i in range(N):
            a, b = fh.readline().strip().split(" ")
            compartments.append((int(a), int(b)))

    print("%s compartments" % N)
    print(compartments)

    initial_compartment = random.randrange(0, N)
    print(initial_compartment)

    while True:
        break


if __name__ == '__main__':
    main()
