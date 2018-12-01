"""
    Name: Special Pythagorean triplet.

    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
        a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.

    ---------------------------------------------------------------

    That is,
    Solve the equation system.
        a^2 + b^2 - c^2 = 0
    AND a + b + c = 1000

"""
def solve_equation():
    for c in range(400, 1000):
        for b in range(200, c):
            for a in range(200, b):
                if (a**2 + b**2 == c**2) and (a + b + c == 1000):
                    return (a, b, c)

    return (-1, -1, -1)

a, b,c = solve_equation()
print(a, b, c)
