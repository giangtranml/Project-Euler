def problem_1():
    """
        Name: Multiples of 3 and 5.

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


def problem_2():
    """
        Name: Even Fibonacci numbers.

        Each new term in the Fibonacci sequence is generated by adding the previous
            two terms. By starting with 1 and 2, the first 10 terms will be:
                1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

        By considering the terms in the Fibonacci sequence whose values do not
            exceed four million, find the sum of the even-valued terms.
    """
    one = 1
    two = 2
    fib = 0
    S = 2
    while fib <  4e6 + 1:
        fib = one + two # 3, 5, 8
        if fib % 2 == 0:
            S += fib
        one = two # 2, 3
        two = fib # 3, 5
    print(S)

def problem_3():
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
    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    prime_set = set()
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

def problem_4():
    """
        Name: Largest palindrome product.

        A palindromic number reads the same both ways.
        The largest palindrome made from the product of
                two 2-digit numbers is 9009 = 91 × 99.

        Find the largest palindrome made from the product
                of two 3-digit numbers.

        --------------------------------------------------------------

        A palindromic number is a number that its original and reversed is
                    equal.
    """
    def reversed_num(num):
        r_num = 0
        while num//10 > 0:
            r_num += num % 10
            r_num *= 10
            num //= 10
        return r_num

    def is_palindrome(num):
        reversed = reversed_num(num)
        if num == reversed:
            return True
        return False

    l_ = []

    for i in range(100, 1000):
        for j in range(100, 1000):
            k = i * j

            if is_palindrome(k):
                l_.append(k)

    res = max(l_)
    print(res)

def problem_5():
    """
        Name: Smallest multiple.

        2520 is the smallest number that can be divided by each of
            the numbers from 1 to 10 without any remainder.

        What is the smallest positive number that is evenly
            divisible by all of the numbers from 1 to 20?

        --------------------------------------------------------------------

        Find LCM(least common multiple) in a range 1 to 20.

        Prime number: 1, 2, 3, 5, 7, 11, 13, 17, 19.

            4         6         8          9      10      12        14      15      16           18         20
           / \       / \       / \        / \     / \     / \       / \     / \     / \         / \         / \
          2   2     2   3     2   4      3   3   2   5   2   6     2   7   3   5   2  8        2   9       2  10
                                 / \                        / \                      / \          / \         / \
                                2   2                      2   3                    2   4        3   3       2   5
                                                                                       / \
                                                                                      2   2
          28              35                 12             32
        2   14          5    7             2    6         2    16
           2  7                               2   3          2    8
                                                                2   4
                                                                   2  2

            | Prime factor
        ----------------------------------------------------------------
         01 | 1
         02 |   2
         03 |               3
         04 |   2  2
         05 |                       5
         06 |   2           3
         07 |                           7
         08 |   2  2  2
         09 |               3   3
         10 |   2                   5
         11 |                                   11
         12 |   2  2        3
         13 |                                           13
         14 |   2                       7
         15 |               3       5
         16 |   2  2  2  2
         17 |                                               17
         18 |   2           3   3
         19 |                                                   19
         20 |   2  2                5

         LCM(1, 20) = 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19

         That is, get the longest sequence length of a factor prime.
    """
    n = 1
    for i in range(2, 21):
        n *= i

    print(n)

def problem_6():
    """
        Name: Sum square difference.

        The sum of the squares of the first ten natural numbers is,
            1^2 + 2^2 + ... + 10^2 = 385
        The square of the sum of the first ten natural numbers is,
            (1 + 2 + ... + 10)^2 = 55^2 = 3025
        Hence the difference between the sum of the squares of the
            first ten natural numbers and the square of
            the sum is 3025 − 385 = 2640.

        Find the difference between the sum of the squares of
            the first one hundred natural numbers and the square of the sum.
    """

    sum_of_square = 0
    square_of_sum = 0
    for i in range(1, 101):
        square_of_sum += i
        sum_of_square += i**2
    square_of_sum **= 2
    print(sum_of_square)
    print(square_of_sum)
    diff = square_of_sum - sum_of_square
    print(diff)

problem_6()
