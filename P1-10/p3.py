import math

def is_prime(num):
    for i in range(2, math.ceil(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

"""
    Name: Largest prime factor.

    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?

    -------------------------------------------------------------------

    Let n = 600851475143

    Let S is prime factorization set of num n. S = {x1, x2, x3, ...}
        every x is prime number. That is, x1*x2*x3*... = n.
    --> The problem find the max prime number of S: result = max(S).

    E.x:
            24
           /  \
          2   12
             /  \
            2    6
                / \
               2   3
"""

def factor_tree(num):
    child = num
    i = 2
    res = 0
    while i < child:
        if is_prime(child):
            res = child
            break
        if child % i == 0:
            child //= i
            i = 1
        i += 1
    return res

n = 600851475143
res = factor_tree(n)
print(res)
