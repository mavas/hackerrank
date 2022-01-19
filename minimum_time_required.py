"""
This is my most difficult problem so far, but I whipped up this solution first,
and it passed some test cases on HackerRank.  I submitted it, and did indeed
think it wouldn't scale, and surely it failed on some test cases, with one
saying "Time limit exceeded", but I think I intuitively know why.

January 19, 2022
"""


def minimum_time_required(machines, goal):
    day_number = 0
    amount_produced_so_far = 0

    while amount_produced_so_far < goal:
        day_number += 1
        #print("Day", day_number)

        machines_today = False
        for machine in machines:
            if (day_number % machine) == 0:
                machines_today = True
                amount_produced_so_far += 1
                #print("\t", machine, amount_produced_so_far)
        if not machines_today:
            #print("\tNo machines today")
            pass

    return day_number


assert minimum_time_required([2, 3], 5) == 6
