try:
    price = float(input("Enter a price: "))
    quantity = int(input("Enter a quantity: "))
    total = price * quantity

except ValueError:
    print("Error: Both price and quantity must be valid numbers!")  

else:
    print(f"The total price is {total} GEL")