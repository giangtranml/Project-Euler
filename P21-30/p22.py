"""
    Names scores

    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
        over five-thousand first names, begin by sorting it into alphabetical order.
        Then working out the alphabetical value for each name, multiply this value by
        its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN,
        which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
        So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
"""
def solve(file_name):
    with open(file_name, "r") as f:
        content = f.read()
    names = sorted(content.replace("\"", "").split(","))
    alpha_scores = {}
    A_int = ord("A")
    Z_int = ord("Z")
    for i in range(A_int, Z_int+1):
        alpha_scores[chr(i)] = i % 64
    res = 0
    for i, word in enumerate(names):
        temp = 0
        for ch in word:
            temp += alpha_scores[ch]
        res += temp*(i+1)
    return res

print(solve("names_prob_22.txt"))
