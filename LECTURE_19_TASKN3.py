phonebook = {
   "giorgi": 557,
   "ana": 445,
   "nika": 777,
   "mariami": 888
}


phonebook.get("giorgi", "not found")

phonebook.setdefault("ja", 444)
phonebook.setdefault("nodo", 333)
phonebook.setdefault("rusa", 111)

name = input("enter a  name: ")
result = phonebook.get(name, "not found")
print(result)