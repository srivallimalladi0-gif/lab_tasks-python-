n = int(input("Enter N: "))
largest = int(input("Enter number: "))

for i in range(n-1):
    x = int(input("Enter number: "))
    if x > largest:
        largest = x

print("Largest =", largest)
