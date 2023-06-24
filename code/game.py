import fileinput
import random


def main():
    score = 0

    with fileinput.input() as fh:
        N = int(fh.readline().strip())

        compartments = [] * N

        compartments_2 = dict()
        compartment_counter = 0

        for i in range(N):
            a, b = fh.readline().strip().split(" ")
            a, b = int(a), int(b)

            compartments.append((a, b))
            compartments_2[compartment_counter] = (a, b)
            compartment_counter += 1

    print("%s compartments" % N)
    print(compartments)
    print(compartments_2)

    initial_compartment = random.randrange(0, N)
    print(initial_compartment)

    while True:
        break


if __name__ == '__main__':
    main()
