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

    current_compartment = random.randrange(0, N)

    while True:
        # Add the player's score, based on the current compartment that the
        # ball is in.  This is a constant operation.
        score += compartments_2[current_compartment]

        # Determine if the ball is going to exit at this time, or move on to
        # the next compartment.  This should be a boolean value.
        going_to_exit = random.randrange(0, N)

        # Either actually exit the entire game and display results, or move the
        # ball to the next compartment and continue the game.
        if going_to_exit:

            score += compartments_2[current_compartment][1]

        else:
            if current_compartment == N:
                current_compartment = 0
            else:
                current_compartment += 1


if __name__ == '__main__':
    main()
