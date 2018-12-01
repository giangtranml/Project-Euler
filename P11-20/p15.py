"""
    Starting in the top left corner of a 2×2 grid,
    and only being able to move to the right and down,
    there are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20×20 grid?

    -------------------------------------------------------------------

    Dynamic Programming Approach:

    -------------------------
    | 2 | 3 | 4 | 5 | 6 | 7 |
    -------------------------
    | 3 | 6 | 10| 15| 21| 28|
    -------------------------
    | 4 | 10| 20| 35|   |   |
    -------------------------
    | 5 | 15| 35| 70|   |   |
    -------------------------
    | 6 |   |   |   |   |   |
    -------------------------
    | 7 |   |   |   |   |   |
    -------------------------

    This approach not only works for the square but also for the rectangle.

    --------------------------------------------------------------------
"""

n = 20
path = [[1]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 and j > 0:
            path[i][j] = path[i][j-1] + 1
            continue
        if j == 0 and i > 0:
            path[i][j] = path[i-1][j] + 1
            continue
        path[i][j] = path[i-1][j] + path[i][j-1]

for p in path:
    print(p)
print(path[n-1][n-1])
