class User():
    status = "Active"


    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age


    def get_info(self):
        print(f"username: {self.username}")
        print(f"email: {self.email}")
        print(f"age: {self.age}")




user_1 = User("JJ88", "Jishkariani@gmail.com", 24)
user_2 = User("JI1", "LINN@gmail.com", 28)
print("=" * 40)
user_1.get_info()
print('=' * 40)
user_2.get_info()      
print('=' * 40)
print(f"user_1: {user_1.status}")
print('=' * 40)
print(f"user_2: {user_2.status}")