fruit = [
    ['Apples', 12, 'AAA'], ['Oranges', 1, 'B'],
    ['Pears', 2, 'A'], ['Grapes', 14, 'UR']]

cars = [
    ['Cadillac', ['Black', 'Big', 34500]],
    ['Corvette', ['Red', 'Little', 1000000]],
    ['Ford', ['Blue', 'Medium', 1234]],
    ['BMW', ['White', 'Baby', 7890]]
]

languages = [
    ['Python', ['Slow', ['Terrible', 'Mush']]],
    ['JavaSCript', ['Moderate', ['Alright', 'Bizarre']]],
    ['Perl6', ['Moderate', ['Fun', 'Weird']]],
    ['C', ['Fast', ['Annoying', 'Dangerous']]],
    ['Forth', ['Fast', ['Fun', 'Difficult']]],
]

x1 = cars[1][1][1]
x2 = cars[1][1][0]
x3 = cars[1][0]
x4 = cars[3][1][1]
x5 = fruit[3][2]
x6 = languages[0][1][1][1]
x7 = fruit[2][1]
x8 = languages[3][1][0]

print(f"{x1} {x2} {x3} {x4} {x5} {x6} {x7} {x8}")