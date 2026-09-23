Pin_Code = "1234"
Pin = input("Please Enter Your Pin Code: ")
tries = 0



while Pin != Pin_Code and tries < 3:
    print(f"Incorrect Pin.Remaining attempts: {3-tries}")
    Pin = input("Please enter your pin code: ")
    tries += 1

if Pin == Pin_Code:
    print("Access Granted!")

else:
     print("card blocked!")














