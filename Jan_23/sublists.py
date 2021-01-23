# Python allows us to store sublists: list inside lists
digits = [[1,2,3], [4,5,6], [7,8,8]]
digits[0:2][0][0] == 1

words = [['abc', 'bcd', 'cde'], [1,2,3], [True, False, True]]
words[:1][0][0] == 'a'

digits = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

len(digits)

digits[0][2]

