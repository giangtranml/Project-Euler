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
