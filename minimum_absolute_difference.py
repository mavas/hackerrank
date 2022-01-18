"""Solved this today by increasing this variable from 100,000 to 1,000,000,
after opening up a test case using a HackerRank hacko, explained here:
https://help.hackerrank.com/hc/en-us/articles/115013862347-Hackos-and-rewards-purchases
.  The new test case gave good insite about simply understanding problem size,
could solve the problem."""


LOWEST_SO_FAR = 1000000


def sorted_minimumAbsoluteDifference(arr):
    """This first sorts the input sequence."""
    arr = sorted(arr)
    i = 0
    lowest_so_far = LOWEST_SO_FAR

    while i < (len(arr) - 1):
        first_value = arr[i]
        second_value = arr[i+1]
        result = abs(first_value - second_value)
        if result < lowest_so_far:
            lowest_so_far = result
        i += 1

    return lowest_so_far


def minimumAbsoluteDifference(arr):
    """This is what I whipped up first, and then I submitted it, and it looks
    like it failed on some test cases specifically due to run time; but surely,
    a lot of the test cases pass, so it's likely an efficiency problem, because
    surely this method isn't too efficient, but good first try to pass some
    cases.  January 17, 2022"""
    lowest_so_far = LOWEST_SO_FAR

    for index_i, i in enumerate(arr):
        for index_j, j in enumerate(arr):
            if index_i != index_j:
                result = abs(i - j)
                if result < lowest_so_far:
                    lowest_so_far = result
 
    return lowest_so_far


if __name__ == '__main__':
    assert minimumAbsoluteDifference([3, -7, 0]) == 3
    assert sorted_minimumAbsoluteDifference([3, -7, 0]) == 3

    d = "962226917 792624362 182480605 599605172 305625864 -81890988 672152087 -133378770 518530121 117194629 417799030 495022422 324358717 546432027 -964011537 -202521429 933382965 -636579333 -228322129 -56148272 765550188 -51728932 354422864 571036550 893033573 -632357224 230731537 957889690 -663303451 -681076766 850996627 796245935 -559647626 417083229 -555235827 -142871142 -265891342 216458754 -852793466 -629971246 -133880688 995384337 -792521943 276619340 391715447 369467242 -534628080 -529731961 159022806 12166614 -227099467 -340866802 -971186523 -292169152 -28963329 646052689 -3201546 -124238932 437046414 -992130998 46703511 290679769 29717534 -30334005 290115457 370682763 774552713 -405804880 416048754 594286847 718627398 -948572155 -955461030 -757111933 -217884128 -445764058 373256233 646756393 525687205 -71009539 -98598593 -361919562 -158639863 937486409 -180417430 916000073 -624472555 -568865371 -248713900 224013616 -741024587 88191350 -319295302 360654385 -973046747 -880171075 -301625980 642186024 123941140 -46393995"
    d = d.split(" ")
    d = [int(x) for x in d]
    assert len(d) == 100
    print(minimumAbsoluteDifference(d))
    #assert sorted_minimumAbsoluteDifference(d) == 501918
    print(sorted_minimumAbsoluteDifference(d))
