balance = 1000

def deposit():
    global balance
    balance += 500
    print("After Deposit =", balance)

def show():
    balance = 200
    print("Local Balance =", balance)

deposit()
show()

print("Global Balance =", balance)
