import csv

def filter_companies():
    large_companies = []

    with open("ssl_companies.csv", "r") as f:
        reader = csv.DictReader(f, delimiter='\t')
        
        for i in reader:
            if i["Number of employees"] > "1000":
                large_companies.append(i)

    return large_companies                
result =filter_companies()
for i in result:
    print(i)

def save_sorted_companies(data):
    if not data:
        print("theres no companies with 1000 employees")
        return
    headers = ["Name", "Industry", "Number of employees"]    
    with open("sorted_companies.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for company in data:
            filtered_row = {
            "Name": company.get("Name"),
            "Industry": company.get("Industry"),
            "Number of employees": company.get("Number of employees")
        }
            writer.writerow(filtered_row)

save_sorted_companies(result)        



