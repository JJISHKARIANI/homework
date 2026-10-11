# from functools import wraps

# def require_role(allowed_role="admin"):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             user_role = kwargs.get("user_role")
#             if user_role == allowed_role:
#                 return func(*args, **kwargs)
#             else:
#                 print(f"permission denied: user is not a {allowed_role}")
#                 return None
#         return wrapper
#     return decorator

# @require_role(allowed_role="admin")
# def my_function(user_role="admin"):
#     print("succesfully") 
#     return "done"

# my_function(user_role="admin")




















