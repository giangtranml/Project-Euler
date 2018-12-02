"""
    Amicable numbers

    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
        therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.

    -------------------------------------------------------------------------

    The idea:
    - Init an array with the length is 10000, the index in array represents
    for n, and the value at that index n is d(n).
    - For each number in range(10000 -> 1): (corresponding the index of array)
        -- find proper divisors of that number, name pd
        -- if that number > length 10000, then move to the next number
        -- if value of arr[pd] == num, then add it to the sum
        -- assign pd at that index. 
"""

arr = [0]*10001

total = 10000

def proper_divisors(num):
    sum = 0
    for i in range(1, num//2 + 1):
        if num % i == 0:
            sum += i
    return sum

res = 0

for n in range(10000, 0, -1):
    sum_div = proper_divisors(n)
    if sum_div > 10000:
        continue
    if arr[sum_div] == n:
        res += n + sum_div
    arr[n] = sum_div

print(res)
