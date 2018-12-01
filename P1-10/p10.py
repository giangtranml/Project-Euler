"""
      Name: Summation of primes

      The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
      Find the sum of all the primes below two million.
  """
  sum = 5
  for i in range(5, int(2e6)):
      if is_prime(i):
          sum += i
  print(sum)
