n = int(input("Enter number: "))
sum = 0

while n > 0:
    r = n % 10
    sum += r
    n //= 10

print("Sum of digits =", sum)
