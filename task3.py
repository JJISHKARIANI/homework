text = input("Enter text: ")
result = ""

for i in text:
    if  i .isdigit():
        continue
    result += i

print(result)