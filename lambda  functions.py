# lambda_functions
from functools import reduce


def add_two_numbers(a, b):
    return a + b


print(add_two_numbers(5, 10))

add_two = lambda a, b: a + b

print(add_two(5, 6))

scores = [{"eng: 56", "mat:78"},
          {"eng: 54", "mat:70"},
          {"eng: 86", "mat:48"},
          {"eng: 47", "mat:90"}, ]

sorted_by_math = sorted(scores, key=lambda s: s['mat'])

print(sorted_by_math)


def get_eng_score(eng_score):
    return eng_score['eng']


sorted_by_eng = sorted(scores, key=get_eng_score)

print(sorted_by_eng)

ages = [12, 34, 64, 76, 57, 90, 110, 120, 130, 140, 150, 160, 170, 89, 23, 90]

total_age = reduce(lambda x, y,: x + y, ages, 0)

print(total_age)

new_ages = map(lambda x: x + 1, ages)
print(new_ages)

above_60 = filter(lambda age: age > 60, ages)
print(list(above_60))
