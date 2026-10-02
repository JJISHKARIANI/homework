student = {
    "name": "jaba",
    "contacts":{
        "phone": 111-222-333,
        "email": "jaba@gmail.com",
    },
    "course":{
        "python":{
            "score": 100,
            "web":{
                "passed": False
        },    
        
            }
        
     }
}

print(student["contacts"]["email"])
print(student["course"]["python"]["score"])
student["course"]["python"]["web"]["passed"] = True
student["course"]["python"]["score"] = 65
del student["contacts"]["phone"]
print(student)