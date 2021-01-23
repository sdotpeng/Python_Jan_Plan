digits = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# 1) Explore copying middle row then changing the item in the copy
# middleRow = digits[1]
# print(middleRow)
# middleRow[0] = -999
# print(middleRow)
# print(digits)

# 2) Explore copying lst two rows then modifying the copy
# firstTwo = digits[0:2]
# print(firstTwo)
# firstTwo[0][0] = -999
# firstTwo[1][1] = 999
# print(firstTwo)
# print(digits)

# 3) Access single int, then change it
# theFour = digits[1][0]
# print(theFour)
# theFour = -999
# print(theFour)
# print(digits)

# 4) How to assign/update valeus of an item in a list of lists?
# digits[1][0] = -9999
# print(digits)

# 5) Access a list of basic types, but not of one the original sublists
# e.g. the lst two ints in the first sublist
# slice = digits[1][:]
# print(slice)
# slice[0] = -999
# print(slice)
# print(digits)