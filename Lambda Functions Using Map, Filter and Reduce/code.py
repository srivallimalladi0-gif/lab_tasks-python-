from functools import reduce

a = [1, 2, 3, 4, 5]

square = list(map(lambda x: x*x, a))
print("Squares:", square)

even = list(filter(lambda x: x%2 == 0, a))
print("Even Numbers:", even)

total = reduce(lambda x, y: x+y, a)
print("Sum:", total)
