"""
    The following iterative sequence is defined for the set of positive integers:

        n → n/2 (n is even)
        n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
"""
MAX = int(1e6)
res = 0
max_length = 0
for i in range(MAX-1, 2, -1):
    num = i
    chains = 0
    while num > 2:
        if num % 2 == 0:
            num //= 2
        else:
            num = num*3 + 1
        chains += 1

    print(chains)
    if max_length < chains:
        max_length = chains
        res = i
print(res)
