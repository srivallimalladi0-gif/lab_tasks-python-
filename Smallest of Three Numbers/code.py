a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a < b:
    if a < c:
        print("Smallest =", a)
    else:
        print("Smallest =", c)
else:
    if b < c:
        print("Smallest =", b)
    else:
        print("Smallest =", c)
