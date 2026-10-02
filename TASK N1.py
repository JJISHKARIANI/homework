try:
    price = float(input("Enter a price: "))
    quantity = int(input("Enter a quantity: "))
    total = price * quantity

except ValueError:
    print("Error: Both price and quantity must be valid numbers!")  

else:
    print(f"The total price is {total} GEL")



















try:
    price = float(input("Enter a price: "))
    quantity = int(input("Enter a quantity: " ))
    total = price * quantity               
    print(total)

except ValueError:
    print("Both price and quantity must be a valid numbers")



else:
    print(f"Total is {total}")






# try:
#     age = int(input("Enter a age: "))
#     if age < 0:
#         raise ValueError("age cannot be negative number")
#     elif age < 18:
#         raise ValueError("age must be at least 18")

# except ValueError as e:
#     print(e)

# finally:
#     print("the code is done")





# try:
#     fruits = ["apple", "banana", "cherry", "orange"]
#     index = int(input("Enter a index of selected fruit: "))
#     selected_fruits = fruits[index]
#     print(f"selected fruit is {selected_fruits} ")

# except ValueError:
#     print("invalid input.enter a whole number")

# except IndexError:
#     print(f"index out of bounds.please chose a index between 0 and {len(fruits)-1}")     

# else:
#     print("Successfully retrieved item")






    









# try:
#     fruits = ["apple", "banana", "cherry", "orange"]
#     index = int(input("Enter a index: "))
#     selected_fruits = fruits[index]
#     print(f"selected fruit is {selected_fruits}")

# except ValueError:
#     print("invalid. enter a whole number")


# except IndexError:
#     print(f"index out of bounds. enter index from 0 to {len(fruits)-1}")


# else:
#     print("Successfully retrieved item")






# try:
#     age = int(input("Enter your age: "))
#     current_year = 2026
#     calculated_year = current_year - age
#     print(calculated_year)



# except ValueError:
#     print("Enter only digits")


# try:
#     password = input("Enter a password: ")

#     if len(password) < 6:
#         raise ValueError("Password is too short")

# except ValueError as e:
#     print(e)