"""
    By starting at the top of the triangle below and moving to adjacent
    numbers on the row below, the maximum total from top to bottom is 23.

        3
        7 4
        2 4 6
        8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom in triangle.txt

    ---------------------------------------------------------------------------

    The approach is starting from second bottom most to top.

    For each number(index j) in the row index i of triangle, we compute:
        triangle[i][j] = triangle[i][j] + max(triangle[i+1][j], triangle[i+1][j+1])

    The result is the top most of the triangle.
"""

def solve(file_name):
    triangle = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            row = list(map(int, line.strip().split(" ")))
            triangle.append(row)

    n = len(triangle)

    for i in range(n-2, -1, -1):
        m = len(triangle[i])
        for j in range(m):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    print(triangle)

solve("../triangle_prob_67.txt")
