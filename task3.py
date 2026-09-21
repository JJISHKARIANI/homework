entered_pin = input("Enter Your Pin Code: ")
correct_pin = "1234"
requested_amount = input("Enter Your Requested Amount: ")
balance = "100$"


if entered_pin == correct_pin:
    print("Correct PIN → Move to the second check")
    

    if balance >= requested_amount:
        print("Enough → Subtract amount from balance and print:")
    else:
        print("Not enough  →  Amount of your balance is not enough.")

else:
    print("Wrong PIN → Incorrect PIN. Access Denied.")