Cart_total = input("Enter a Cart Total: ")
is_vip = input("Are you a Vip?: ")
P_code = input("Enter a  promo code: ")
is_guest = input("Are you a guest?: ") 
Promo_Code = "SAVE10"


if Cart_total >= "50" or is_vip:
    print("You got a free shipping")

if Promo_Code !="" and not is_guest == "yes":
    print("You got 10% discount")
