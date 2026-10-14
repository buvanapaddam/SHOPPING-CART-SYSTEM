# Shopping Cart System
# Mini Project Using Python Lists

product_list = []
cart_list = []
user_list = []
order_list = []

while True:
    print("\n===== SHOPPING CART SYSTEM =====")
    print("1. Admin")
    print("2. User")
    print("3. Exit")

    role = input("Select your role: ")

    # ADMIN SECTION
    if role == "1":
        admin_name = input("Enter admin name: ")

        while True:
            print("\n===== ADMIN MENU =====")
            print("1. Add Product")
            print("2. Update Product")
            print("3. Remove Product")
            print("4. View Products")
            print("5. View Users")
            print("6. View Orders")
            print("7. Exit")

            choice = input("Enter your choice: ")

            # Add Product
            if choice == "1":
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter quantity: "))

                product = [name, price, quantity]
                product_list.append(product)

                print("Product added successfully!")

            # Update Product Price
            elif choice == "2":
                name = input("Enter product name to update: ")
                found = False

                for product in product_list:
                    if product[0].lower() == name.lower():
                        product[1] = float(
                            input("Enter new price: ")
                        )
                        print("Product updated successfully!")
                        found = True
                        break

                if not found:
                    print("Product not found!")

            # Remove Product
            elif choice == "3":
                name = input("Enter product name to remove: ")
                found = False

                for product in product_list:
                    if product[0].lower() == name.lower():
                        product_list.remove(product)
                        print("Product removed successfully!")
                        found = True
                        break

                if not found:
                    print("Product not found!")

            # View Products
            elif choice == "4":
                print("\nAvailable Products:")

                if len(product_list) == 0:
                    print("No products available.")
                else:
                    for product in product_list:
                        print(
                            "Name:", product[0],
                            "| Price:", product[1],
                            "| Quantity:", product[2]
                        )

            # View Users
            elif choice == "5":
                print("\nRegistered Users:")

                if len(user_list) == 0:
                    print("No users registered.")
                else:
                    for user in user_list:
                        print(user)

            # View Orders
            elif choice == "6":
                print("\n===== ORDER DETAILS =====")

                if len(order_list) == 0:
                    print("No orders placed.")
                else:
                    for order in order_list:
                        print("User:", order[0])
                        print("Products:", order[1])
                        print("Total Amount: Rs.", order[2])
                        print("--------------------")

            # Admin Exit
            elif choice == "7":
                print("Admin logged out.")
                break

            else:
                print("Invalid choice!")

    # USER SECTION
    elif role == "2":
        user_name = input("Enter your name: ")

        if user_name not in user_list:
            user_list.append(user_name)

        # Each user's cart is stored separately.
        cart_list = []

        while True:
            print("\n===== USER MENU =====")
            print("1. View Products")
            print("2. Add to Cart")
            print("3. Remove from Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Exit")

            choice = input("Enter your choice: ")

            # View Products
            if choice == "1":
                print("\nAvailable Products:")

                if len(product_list) == 0:
                    print("No products available.")
                else:
                    for product in product_list:
                        print(
                            "Name:", product[0],
                            "| Price:", product[1],
                            "| Quantity:", product[2]
                        )

            # Add to Cart
            elif choice == "2":
                if len(product_list) == 0:
                    print("No products available.")
                    continue

                print("\nAvailable Products:")
                for product in product_list:
                    print(
                        "Name:", product[0],
                        "| Price:", product[1],
                        "| Quantity:", product[2]
                    )

                name = input("Enter product name: ")
                found = False

                for product in product_list:
                    if product[0].lower() == name.lower():
                        found = True

                        if product[2] > 0:
                            quantity = int(
                                input("Enter quantity: ")
                            )

                            if quantity > 0 and quantity <= product[2]:
                                cart_list.append(
                                    [product[0], product[1], quantity]
                                )

                                product[2] -= quantity
                                print("Product added to cart!")
                            else:
                                print(
                                    "Invalid quantity or insufficient stock."
                                )
                        else:
                            print("Product is out of stock!")

                        break

                if not found:
                    print("Product not found!")

            # Remove from Cart
            elif choice == "3":
                if len(cart_list) == 0:
                    print("Your cart is empty.")
                else:
                    name = input(
                        "Enter product name to remove from cart: "
                    )
                    found = False

                    for item in cart_list:
                        if item[0].lower() == name.lower():
                            for product in product_list:
                                if product[0] == item[0]:
                                    product[2] += item[2]
                                    break

                            cart_list.remove(item)
                            print("Product removed from cart!")
                            found = True
                            break

                    if not found:
                        print("Product not found in cart!")

            # View Cart
            elif choice == "4":
                if len(cart_list) == 0:
                    print("Your cart is empty.")
                else:
                    print("\n===== YOUR CART =====")
                    total = 0

                    for item in cart_list:
                        subtotal = item[1] * item[2]
                        total += subtotal

                        print(
                            "Name:", item[0],
                            "| Price:", item[1],
                            "| Quantity:", item[2],
                            "| Subtotal:", subtotal
                        )

                    print("Total Amount: Rs.", total)

            # Checkout
            elif choice == "5":
                if len(cart_list) == 0:
                    print("Your cart is empty.")
                else:
                    total = 0

                    for item in cart_list:
                        total += item[1] * item[2]

                    print("\n===== CHECKOUT =====")
                    print("Customer:", user_name)
                    print("Total Amount: Rs.", total)

                    confirm = input(
                        "Confirm your order? (yes/no): "
                    ).lower()

                    if confirm == "yes":
                        order_items = [
                            item.copy() for item in cart_list
                        ]

                        order_list.append(
                            [user_name, order_items, total]
                        )

                        cart_list.clear()
                        print("Order placed successfully!")
                        print("Thank you for shopping.")
                    else:
                        print("Order cancelled.")

            # User Exit
            elif choice == "6":
                print("User logged out.")
                break

            else:
                print("Invalid choice!")

    # Main Exit
    elif role == "3":
        print("Thank you for using Shopping Cart System!")
        break

    else:
        print("Invalid role! Please select again.")
