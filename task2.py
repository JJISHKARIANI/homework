n = int(input("Enter a postive integer: "))
total_sum = 0

for i  in range(2, n + 1, 2):
    total_sum += i

print(f"The sum of even numbers from 1 to {n} is: {total_sum}")