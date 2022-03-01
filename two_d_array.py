"""
https://www.hackerrank.com/challenges/2d-array/problem

I guess I couldn't figure this one out just yet; still not done.
"""


def main(arr):
    max_so_far = -99999
    x = 1
    y = 1
    count = 0

    while x <= 4:
        y = 1
        while y <= 4:
            top = arr[x-1][y-1] + arr[x-1][y] + arr[x-1][y+1]
            middle = arr[x][y]
            bottom = arr[x+1][y-1] + arr[x+1][y] + arr[x+1][y+1]
            total = top + middle + bottom
            if total > max_so_far:
                count += 1
                max_so_far = total
            y += 1
        x += 1
    print(count)

    return max_so_far


if __name__ == '__main__':
    arr = [[1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]]
    main(arr)
    arr = [[-1, -1, 0, -9, -2, -2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5]]
    main(arr)
