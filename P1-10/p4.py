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
