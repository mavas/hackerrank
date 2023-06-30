"""
3
1 100
1 100
1 1
"""


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
            compartments_2[compartment_counter] = {'scores': (a, b), 'prob': random.uniform(0.01, 0.99)}
            compartment_counter += 1

    print("%s compartments" % N)
    s = 0
    for k, v in compartments_2.items():
        print("\t%s, %s" % (k, v))
        s += v['scores'][0] * v['prob']
    print("sum: %s" % s)
    print("sum: %s" % (s+4))
    print(compartments)
    print(compartments_2)

    current_compartment = random.randrange(0, N)

    while True:
        # Add the player's score, based on the current compartment that the
        # ball is in.  This is a constant operation.
        score += compartments_2[current_compartment]['scores'][0]
        choice = random.uniform(0.01, 0.99)
        print("choice: %s, current_bucket_prob: %s" % (choice, compartments_2[current_compartment]['prob']))
        break

        # Determine if the ball is going to exit at this time, or move on to
        # the next compartment.  This should be a boolean value.
        going_to_exit = random.randrange(0, N)

        # Either actually exit the entire game and display results, or move the
        # ball to the next compartment and continue the game.
        if going_to_exit:

            score += compartments_2[current_compartment][1]
            break

        else:
            if current_compartment == N:
                current_compartment = 0
            else:
                current_compartment += 1


if __name__ == '__main__':
    main()
