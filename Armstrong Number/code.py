n = int(input("Enter 3 digit number: "))
temp = n
sum = 0

while n > 0:
    r = n % 10
    sum += r ** 3
    n //= 10

if temp == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
