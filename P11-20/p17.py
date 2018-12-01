"""
    If the numbers 1 to 5 are written out in words: one, two, three, four,
        five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    If all the numbers from 1 to 1000 (one thousand) inclusive were
        written out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342
        (three hundred and forty-two) contains 23 letters and 115
        (one hundred and fifteen) contains 20 letters. The use of "and"
        when writing out numbers is in compliance with British usage.
"""
chars = """one, two, three, four, five, six, seven, eight, nine, ten,
         eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen,
         eighteen, nineteen, twenty, thirty, forty,
         fifty, sixty, seventy, eighty, ninety
         """
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30,
40, 50, 60, 70, 80, 90]
chars = [c.strip() for c in chars.split(",")]
mapping = {}
for i, v in enumerate(chars):
    mapping[nums[i]] = v
res = 0
for num in range(1, 1001):
    while num > 0:
        if num <= 20:
            res += len(mapping[num])
            num = 0
        elif num > 20 and num < 100:
            temp = num
            temp -= temp % 10
            res += len(mapping[temp])
            num %= 10
        elif num >= 100 and num < 1000:
            _100th = "hundred"
            first = num // 100
            ch = mapping[first] + _100th
            num %= 100
            res += len(ch) if num == 0 else len(ch) + 3
        else:
            _1000th = "thousand"
            first = num // 1000
            ch = mapping[first] + _1000th
            res += len(ch)
            num %= 1000
print(res)
