from math import factorial


n = 100

sum = 0
fact = factorial(n)

while fact > 0:
    sum += fact % 10
    fact //= 10

print(sum)
