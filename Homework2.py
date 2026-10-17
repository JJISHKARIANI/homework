import csv

def surviovors_filter():
    survivors = []

    with open("titanic.csv", "r") as file:
       reader = csv.DictReader(file, delimiter='\t', )
       for i in reader:
          if i["Survived"] == "1":
             survivors.append(i)

    return survivors       

result = surviovors_filter()
for passenger in result:
   print(passenger)



def saved_survivors(data):
  
    if not data:
       print("theres no survivors")
       return

    headers = data[0].keys()
    with open("survived.csv", "w") as f:
       writer = csv.DictWriter(f, fieldnames=headers,)
       writer.writeheader()
       writer.writerows(data)

saved_survivors(result)
