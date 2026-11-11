balance = 1000000

while True:
    print("===== ATM Simulator =====")
    print("1. Show Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = int(input("Please choose an option: "))

    if choice == 1:
        print(balance)

    elif choice == 2:
        print("Withdraw")
        withdraw = int(input("Please enter the amount: "))
        if 0 < withdraw <= balance:
            balance = balance - withdraw
            print("Your new balance is:", balance)
        else:
         print("Invalid amount or insufficient balance!")

    elif choice == 3:
        print("Deposit")
        deposit = int(input("Please enter the amount: "))
        if deposit > 0:
           balance = balance + deposit
           print("Your new balance is:", balance)
        else:
           print("Invalid amount or insufficient balance!")

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid option!")