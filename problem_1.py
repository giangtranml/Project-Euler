"""
    If we list all the natural numbers below 10 that are multiples
        of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.

    -------------------------------------------------------------------------

    Let S = {x1, x2, x3, ... } finite set with all x < 1000.
    We need to find x such that x % 3 == 0 and x % 5 == 0.
    The result is the sum of S. (res = sum(S))
"""
res = 0
for i in range(1000):
     if i % 3 == 0 or i % 5 == 0:
         res += i
print(res)
