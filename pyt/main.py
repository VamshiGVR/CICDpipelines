#function
def deposit():
    while True:
        amount = input("Deposit ?$")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("must be >0")
        else:
            print("enter numbers only")
    return amount

def main():
    balance = deposit()

main()