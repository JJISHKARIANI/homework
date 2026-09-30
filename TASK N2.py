student ={
    "name": "ana",
    "contact":{
        "email": "ana@gmail.com",
        "phone": "111-222-333"
    },
    "course":{
        "python":{
            "passed": True,
            "score": 100,
        },
         "web":{
             "passed": False,
             "score": 40
         }
    }
}
   




print("ana's email:", student["contact"]["email"])
print("python score:", student["course"]["python"]["score"])
student["course"]["web"]["passed"] = True
student["course"]["web"]["score"] = 65
print(student)
del student["contact"]["phone"]

