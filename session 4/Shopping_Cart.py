
cart = []

while True:
    print(f'''
    ====== Shopping Cart ======
    1. Add Item
    2. Remove Item
    3. Checkout
    ''')

    choice = int(input("Enter your option: "))

    if choice == 1:
        item_Name = input("Enter Item Name: ")
        item_price = float(input("Enter Item Price: "))

        cart.append((item_Name, item_price))

    elif choice == 2:
        item_remove = input("Enter Item Name to remove: ")

        for item in cart:
            if item[0] == item_remove:
                cart.remove(item)
                print("Item removed successfully!")
                break
        else:
            print("Item not found!")

    elif choice == 3:
        total = sum(item[1] for item in cart)
        tax = total * 0.1
        discount = total * 0.05
        final_price = total + tax - discount

        print("===== Shopping Cart Receipt =====")

        for item in cart:
            print(f"Name: {item[0]} | Price: {item[1]}")

        print(f'''
        Total: {total}
        Tax: {tax}
        Discount: {discount}
        Final Price: {final_price}
        ''')

        break

    else:
        print("Invalid option!")
