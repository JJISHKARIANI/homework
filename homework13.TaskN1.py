def even_numbers():
    num = 0

    while True:
        yield num
        num += 2
        if num > 10:
            break

numbs = even_numbers()  
print(next(numbs))
print(next(numbs))
# print(next)    or          
for item in numbs:
    print(item)