Age = input("Enter Your Age: ")

if Age <= "0":
    print("Invalid age entered")

elif Age < "5" :
   
    print("Your ticket is free")

elif Age <= "12":
    print("Your ticket price is 8$")

elif Age <= "64":
    print("Your ticket price is 15$")

else:
    print("Your Ticket price is 10 $")