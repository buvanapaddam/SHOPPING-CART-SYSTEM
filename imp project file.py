#shopping cart system
#Mini project using python lists

product_list=[]
cart_list=[]
user_list=[]
order_list=[]
while True:
    print("\n===== SHOPPING CART SYSTEM =====")
    print("1.Admin")
    print("2.user")
    print("3.Exit")

    role=input("select your role:")
    
    #ADMIN SECTION
    if role == "1":
        admin_name = input("enter admin name: ")
        while True:
            print("\n===== ADMIN MENU =====")
            print("1. Add product")
            print("2. update product") 
            print("3. Remove product")
            print("4. view products")
            print("5. view users")
            print("6. Exit")

            choice =input("enter your choice:")
            
            #Add products
            if choice == "1":
                name = input("enter product name: ")
                price =float(input("enter product price:"))
                quantity = int(input("enter quantity:"))
                product = [name,priece,quantity]
                product_list.append(product)
                print("product added successfully!")

                #update products
                elif choice == "2":
                    nsme = input("enter product name to update:")
                    found = False
                    for product in product_list:
                        if product[0] == name:
                            product[1] == float(
                                input("enter new quantity: ")
                                )
                            print("product updated successfully!")
                            found = True
                            break
                        if found == False:
                            print("product not found!")
                            
                            #Remove product
                            elif choice == "3":
                                name = input("enter product name to remove: ")
                                found = false

                                for product in product list:
                                    if product_list.remove(product)
                                    print("product removed successfully!")
                                    found = True
                                    break

                                if found == False:
                                    print("product not found!")

                                    #view products
                                    elif choice == "4":
                                        print("\nAvailable products:")

                                        if len(product_list) == 0:
                                            print("NO products available.")
                                            else:
                                                for product in product_list:
                                                    print(
                                                        "Name:",product[0],
                                                        "|price:", product[1],
                                                        "|Quantity:", product[2]
                                                        )

                                                    #view users
                                                    elif choice == "5":
                                                        print("\nRegistered users:")

                                                        if len(user_lists) == 0:
                                                            print("No users registered.")
                                                        else:
                                                            for user in user_lists:
                                                                print(user)

                                                   #Admin Exit
                                                                elif choice == "6":
                                                                    break
                                                                else:
                                                                    print("Invalid choice!")

                                                  #User section
                                                                    elif role == "2":
                                                                        user_name = input("enter your name:")

                                                                        if user_name not on user_list:
                                                                            user_list.appemd(user_name)

                                                                        while True:
                                                                            print("\n===== USER MENU =====")
                                                                            print("1. view products")
                                                                            print("2. Add to cart")
                                                                            print("3. Remove from cart")
                                                                            print("4. view cart")
                                                                            print("5. checkout")
                                                                            print("6. Exit")

                                                                            choice = input("enter your choice: ")

                                                                            #view products
                                                                            if choice == "1"
                                                                                print("\nAvaialble productd:")

                                                                                if lem(product_list) == 0:
                                                                                    print(
                                                                                        "Name:",product[0]
                                                                                        "|price:",product[1],
                                                                                        "|quantity:",product[2]
                                                                                        )

                                                                                    #Add to cart
                                                                                    elif choice == "2":
                                                                                        name = input("enter product name:")
                                                                                        found = False

                                                                                        for product in product_list:
                                                                                            if product[0] == name:
                                                                                                if product[2] > 0:
                                                                                                    cart_list.append(
                                                                                                        [user_name,product[0],product[1]]
                                                                                                        )
                                                                
    
