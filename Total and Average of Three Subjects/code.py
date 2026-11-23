def marks(a, b, c):
    total = a + b + c
    avg = total / 3
    return total, avg

a = int(input("Enter marks 1: "))
b = int(input("Enter marks 2: "))
c = int(input("Enter marks 3: "))

t, av = marks(a, b, c)

print("Total =", t)
print("Average =", av)
