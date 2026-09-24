n = int(input("Enter a postive integer: "))
total_sum = 0

if n < 0:
    print(f"The {n} is not a Positive Integer.)
    exit()
    
for i  in range(2, n + 1, 2):
    total_sum += i

print(f"The sum of even numbers from 1 to {n} is: {total_sum}")
