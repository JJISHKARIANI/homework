inventory = ["apple", "banana", "orange",  "apple","kiwi", "apple"]
new_items = ["mango", "grape"]

print(inventory.count("apple"))
print(inventory.index("orange"))

inventory.extend(new_items)
print(inventory[::-1])