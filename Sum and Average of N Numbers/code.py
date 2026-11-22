n = int(input("Enter N: "))
sum = 0

for i in range(n):
    x = int(input("Enter number: "))
    sum += x

print("Sum =", sum)
print("Average =", sum/n)
