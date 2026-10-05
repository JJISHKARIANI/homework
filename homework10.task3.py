names = ["Laptop", "Phone", "Headphones", "Monitor"]
prices = [1200, 800, 150, 300]
ratings = [4.8, 4.5, 4.2, 4.9]

union = list(zip(names, prices, ratings))
print(union)

sorted_union = sorted(union, key=lambda union: union[1], reverse=True)
print(sorted_union)