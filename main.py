import requests
from models import Joke
from storage import Storage

def fetch_joke_from_api(category="Any"):
    url = f"https://v2.jokeapi.dev/joke/{category}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("error"):
            print("Joke not found") 
            return None

        category = data.get("category")
        joke_type = data.get("type")

        if joke_type == "single":
            return Joke(category, joke_type, joke=data.get("joke"))
        else:
            return Joke(category, joke_type, setup=data.get("setup"), delivery=data.get("delivery"))
    
    except requests.exceptions.ConnectionError:
        print("[error]: Internet connection failed")
        return None
    
    except Exception as e:
        print(f"[error]: {e}")

def main():
    while True:
        print("\n=== Joke Collection ===")
        print("1. New Joke Generator")
        print("2. List of Generated Jokes")
        print("3. Delete Joke From List")
        print("4. Exit")

        choice = input("Enter a Number (option) 1 - 4: ").strip()
        
        if choice == "1":
            print("Categories: Programming, Misc, Dark, Pun, Spooky, Christmas or Any")
            user_category = input("Enter a Category or leave it blank for Any: ").strip().capitalize()

            if not user_category:
                user_category = "Any"

            joke = fetch_joke_from_api(user_category)
            if joke:
                print("Joke has been collected:")
                joke.display()

                save_choice = input("Do you want to save this joke? (y/n): ").strip().lower()
                if save_choice == "y":
                    Storage.add_joke(joke)
                    print("Joke saved successfully!")   

        elif choice == "2":
            jokes = Storage.load_joke()
            if not jokes:
                print("There are no jokes in the list.") 
            else:
                print("\n--- Saved Jokes ---")
                for i in range(len(jokes)):
                    joke = jokes[i]
                    print(f"\n[{i}] Category: {joke.category}")            
                    joke.display()

        elif choice == "3":
            jokes = Storage.load_joke()
            if not jokes:
                print("There are no jokes to delete.")
                continue

            print("\n--- Jokes List ---")
            for i in range(len(jokes)):
                joke = jokes[i]
                print(f"\n--- Joke #{i} (Category: {joke.category}) ---") 
                joke.display()
                
            try:
                idx = int(input("\nEnter the number of the joke to delete: "))
                success = Storage.delete_joke(idx)       
                if success:
                    print("Joke deleted successfully!") 
                else:
                    print("Error: No joke with that index.")

            except ValueError:
                print("Error: Please enter a valid integer.")  

        elif choice == "4":
            print("Goodbye!")
            break                     

        else:
            print("Incorrect choice, Try again.")

if __name__ == "__main__":
    main()