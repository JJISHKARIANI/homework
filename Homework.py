def info():
    author = input("Enter your favorite author: ")
    quotes = input("Enter your favorite quetos: ")
    
    with open("quotes.txt", "a") as file:
        file.write(f"Favorite Author: {author} Favorite Quote: {quotes}")

info()



def info_reader():

    try:
        with open("quotes.txt", "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("file doesnt exist")        

info_reader()        
