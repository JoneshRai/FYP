# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend
# from api.models import CustomUser 
# User = get_user_model()

# class EmailAuthBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         print(f"Trying to authenticate user with email: {username} and password: {password}")

#         try:
#             # Retrieve user by email (username is being used for the email)
#             user = CustomUser.objects.get(email=username)
#             print(f"User found: {user}")

#             # Check if password matches the stored password
#             if user.check_password(password):
#                 print("Password is correct.")
#                 return user
#             else:
#                 print("Password is incorrect.")
#         except CustomUser.DoesNotExist:
#             print(f"No user found with email: {username}")

#         return None




