fruits = ["apple", "banana", "cherry", "orange"]


try:
    index = int(input("Enter a index: "))
    selected_fruits = fruits[index]
    print(f"selected fruits: {selected_fruits}")

except ValueError:
    print("Invalid input. please enter a whole number: ")

except IndexError:
    print(f"index out of bounds. choose a index between 0 and {len(fruits)-1}.")

else:
    print("Successfully retrieved item.")