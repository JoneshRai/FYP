# from rest_framework import viewsets, permissions
# from rest_framework.response import Response
# from django.contrib.auth import authenticate, get_user_model
# from knox.models import AuthToken
# from django.shortcuts import render
# from api.auth_backend import EmailAuthBackend
# from .serializers import LoginSerializer, RegisterSerializer

# from django.core.mail import send_mail
# from django.views.generic.edit import FormView
# from django.views.generic.list import ListView
# from .models import Emails
# from rest_framework.views import APIView
# from .pusher import pusher_client
# from rest_framework import status
# from rest_framework import generics




from rest_framework import viewsets, permissions
from .serializers import *
from .models import *

from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.db.models import Sum
# Restframework
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from datetime import datetime

# Others
import json
import random




User = get_user_model()


class MyTokenObtainPairView(TokenObtainPairView):
    # Here, it specifies the serializer class to be used with this view.
    serializer_class = MyTokenObtainPairSerializer

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

# User = get_user_model()
# def index(request):
#     return render(request, 'gallery.jsx')


class RegisterViewset(generics.CreateAPIView):
    # It sets the queryset for this view to retrieve all User objects.
    queryset = CustomUser.objects.all()
    # It specifies that the view allows any user (no authentication required).
    permission_classes = [AllowAny]
    # It sets the serializer class to be used with this view.
    serializer_class = RegisterSerializer


class LoginViewset(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def create(self, request):
        # Deserialize the incoming data
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email=serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            user=authenticate(request,email=email, password=password)
            
            if user:
                _,token= AuthToken.objects.create(user)
                return Response(
                    {
                        "user": self.serializer_class(user).data,
                        "token":token
                    }
                )
            else:
                return Response({"error":"Invalid Credentials"},status=401)
        else:
            return Response(serializer.errors,status=400)
# class PasswordEmailVerify(generics.RetrieveAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = api_serializer.UserSerializer
    
#     def get_object(self):
#         email = self.kwargs['email']
#         user = api_models.User.objects.get(email=email)
        
#         if user:
#             user.otp = generate_numeric_otp()
#             uidb64 = user.pk
            
#              # Generate a token and include it in the reset link sent via email
#             refresh = RefreshToken.for_user(user)
#             reset_token = str(refresh.access_token)

#             # Store the reset_token in the user model for later verification
#             user.reset_token = reset_token
#             user.save()

#             link = f"http://localhost:5173/create-new-password?otp={user.otp}&uidb64={uidb64}&reset_token={reset_token}"
            
#             merge_data = {
#                 'link': link, 
#                 'username': user.username, 
#             }
#             subject = f"Password Reset Request"
#             text_body = render_to_string("email/password_reset.txt", merge_data)
#             html_body = render_to_string("email/password_reset.html", merge_data)
            
#             msg = EmailMultiAlternatives(
#                 subject=subject, from_email=settings.FROM_EMAIL,
#                 to=[user.email], body=text_body
#             )
#             msg.attach_alternative(html_body, "text/html")
#             msg.send()
#         return user





# class PasswordChangeView(generics.CreateAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = UserSerializer
    
#     def create(self, request, *args, **kwargs):
#         payload = request.data
        
#         otp = payload['otp']
#         uidb64 = payload['uidb64']
#         password = payload['password']

        

#         user = api_models.User.objects.get(id=uidb64, otp=otp)
#         if user:
#             user.set_password(password)
#             user.otp = ""
#             user.save()
            
#             return Response( {"message": "Password Changed Successfully"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response( {"message": "An Error Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# class MessageAPIView(APIView):
#     def get(self, request):
#         # Example: Return a success message for testing the GET method
#         return Response({"message": "GET method is working!"}, status=200)

#     def post(self, request):
#         # Trigger a Pusher event with the provided username and message
#         pusher_client.trigger('chat', 'message', {
#             'username': request.data.get('username'),
#             'message': request.data.get('message'),
#         })
#         return Response({"message": "Message sent!"}, status=201)
    
    
# class LoginVViewset(viewsets.ViewSet):
#     permission_classes =[permissions.AllowAny]
#     serializer_class = LoginSerializer
    
#     def create(self,request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             email=serializer.validated_data['email']
#             password = serializer.validated_data['password']

#             authen = EmailAuthBackend
            
#             user=authen.authenticate(self,email=email, password=password)
            
#             if user:
#                 _,token= AuthToken.objects.create(user)
#                 return Response(
#                     {
#                         "user": self.serializer_class(user).data,
#                         "token":token
                       
#                     }
#                 )
#             else:
#                 return Response({"error":"Invalid Credentials"},status=401)
#         else:
#             return Response(serializer.errors,status=400)


# class RegisterViewset(viewsets.ViewSet):
#     permission_classes = [permissions.AllowAny]
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer

#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             _, token = AuthToken.objects.create(user)
#             return Response({
#                 "user": {
#                     "id": user.id,
#                     "username": user.username,
#                     "email": user.email
#                 },
#                 "token": token
#             })
#         else:
#             return Response(serializer.errors, status=400)



class UserViewSet(viewsets.ReadOnlyModelViewSet):  # Use ReadOnlyModelViewSet for listing data
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RegisterSerializer
    queryset = CustomUser.objects.all()  # Define queryset at the class level

    def list(self, request):
        # You can further filter the queryset or add pagination if needed
        queryset = CustomUser.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)





class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProfileSerializer

    def get_object(self):
        user_id = self.kwargs['user_id']

        user = CustomUser.objects.get(id=user_id)
        profile = Profile.objects.get(user=user)
        return profile
    

# def generate_numeric_otp(length=7):
#         # Generate a random 7-digit OTP
#         otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
#         return otp

    


class CategoryListAPIView(generics.ListAPIView):
    serializer_class =  CategorySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Category.objects.all()
    

class PostCategoryListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        category_slug = self.kwargs['category_slug'] 
        category = Category.objects.get(slug=category_slug)
        return Post.objects.filter(category=category, status="Active")


        
        
class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Post.objects.all() 
    
class PostDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        slug = self.kwargs['slug']
        post = Post.objects.get(slug=slug, status="Active")
        post.view += 1
        post.save()
        return post







class LikePostAPIView(APIView):
    def post(self,request):
        user_id = request.data.get('user_id') 
        post_id = request.data.get('post_id') 

        user = CustomUser.objects.get(id=user_id)
        feed = Post.objects.get(id=post_id)
        
        if user in feed.likes.all():
            feed.likes.remove(user)
            return Response({"message":"Post Disliked"},status=status.HTTP_200_OK)
        else:
            feed.likes.add(user)
            
            # Notif.objects.create(
            #     user=feed.user,
            #     feed=feed,
            #     type="Likes"
            # )
            return Response({"message":"Post Liked"},status=status.HTTP_201_CREATED)


# class  ViewComment(APIView):
#     # serializer_class= ComSerializer
#     # permission_classes=[permissions.AllowAny]
    
#     def post(self,request): 
#                 # serializer = CommentSerializer(data=request.data)
#                 post_id = request.data.get('post_id') 
#                 # fullname= request.data.get('fullname') 
#                 emails = request.data.get('email') 
#                 comment = request.data.get('comment') 

                
            
#                 email = CustomUser.objects.get(email=emails)
#                 post = Post.objects.get(id=post_id)
                
#                 Comment.objects.create(
#                     post=post,
#                     # fullname= fullname,
#                     email=emails,
#                     comment=comment
#                 )
#                 # Notif.objects.create(
#                 #         user=post.user,
#                 #         feed=post,
#                 #         type="Comments"
#                 #     )
#                 # if serializer.is_valid():
#                 #     serializer.save()
#                     return Response(serializer.data, status=status.HTTP_201_CREATED)









# class LikePostAPIView(APIView):
#     def post(self,request):
#         user_id = request.data.get('user_id') or input("Enter user_id: ")
#         post_id = request.data.get('feed_id') or input("Enter post_id: ")

#         user = CustomUser.objects.get(id=user_id)
#         post = Post.objects.get(id=post_id)
        
#         if user in post.likes.all():
#             post.likes.remove(user)
#             return Response({"messsage":"Post Disliked"},status=status.HTTP_200_OK)
#         else:
#             post.likes.add(user)
            
#             Notif.objects.create(
#                 user=post.user,
#                 post=post,
#                 type="Like"
#             )
#             return Response({"message":"Post Liked"},status=status.HTTP_201_CREATED)


class ViewComment(APIView):
    def post(self, request):
        # Get data from request.data (frontend)
        post_id = request.data.get('post_id')
        name = request.data.get('name')
        email = request.data.get('email')
        comment = request.data.get('comment')

        # Validate required fields
        if not (post_id and name and email and comment):
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the post exists
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        # Create Comment
        Comment.objects.create(
            post=post,
            name=name,
            email=email,
            comment=comment
        )

        return Response({"message": "Comment Sent"}, status=status.HTTP_201_CREATED)


class Dashboard(generics.ListAPIView):
    serializer_class = AuthorSerial
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        user_id=self.kwargs['user_id']
        user= CustomUser.objects.get(id=user_id)
        
        views = Post.objects.filter(user=user).aggregate(view=Sum("view"))['view']
        posts = Post.objects.filter(user=user).count()
        likes = Post.objects.filter(user=user).aggregate(totalLikes=Sum("likes"))['TotalLikes']
        
        return[{
            "views":views,
            "posts":posts,
            "likes":likes,
        }]
    def list(self,request,*args, **kwargs):
        queryset= self.get_queryset()
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data)


class DashboardPostlist(generics.ListAPIView):
        serializer_class= PostSerializer
        permission_classes=[permissions.AllowAny]
        
        def get_queryset(self):
           user_id=self.kwargs['user_id']
           user=CustomUser.User.objects.get(id=user_id)
           return Post.objects.filter(user=user).order_by("-id")

class DashboardCommentList(generics.ListAPIView):
        serializer_class=CommentSerializer
        permission_classes=[permissions.AllowAny]
        
        def get_queryset(self):
            user_id=self.kwargs['user_id']
            user=CustomUser.objects.get(id=user_id)
           
            return Comment.objects.filter(post__user=user)

class DashboardCommentReply(APIView):
        
        def post(self,request):
            comment_id = request.data['comment_id']
            reply = request.data['reply']
            
            comment=Comment.objects.get(id=comment_id)
            comment.reply=reply
            
            comment.save()
            
            return Response({"message":"Comment response sent"},status=status.HTTP_201_CREATED)


class DashboardPostCreate(generics.CreateAPIView):
    serializer_class= PostSerializer
    permission_classes= [permissions.AllowAny]
    
    def create(self, request,*args, **kwargs):
        print(request.data)
        
        user_id = request.data.get("user_id")
        title = request.data.get("title")
        description = request.data.get('description')
        image = request.data.get("image")
        comment = request.data.get("comment")
        tags = request.data.get("tags")
        video = request.data.get("video")
        category_id = request.data.get('category')
        status = request.data.get("status")
    
        user= CustomUser.ibjects.get(id=user_id)
        topic = Topic.objects.get(id=topic)
        
        Post.objects.create(
            user=user,
            title=title,
            image=image,
            comment=comment,
            description=description,
            tags=tags,
            video= video,
            category=category,
            status=status
        )
        return Response({"message":"post created successfully!!"},status=status.HTTP_201_CREATED)


class DashboardUpdatePost(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=PostSerializer
    permission_classes=[permissions.AllowAny]
    
    def get_object(self):
        user_id = self.kwargs['user_id']
        user= CustomUser.objects.get(id=user_id)
        post_id=self.kwargs['post_id']
      
        return Post.objects.get(user=user,id=post_id)
    
    def update(self,request,*args, **kwargs):
        post_instance=self.get_object()
        
        title=request.data.get("title")
        image = request.data.get("image")
        description= request.data.get("descrption")
        comment = request.data.get("comment")
        tags = request.data.get("tags")
        category_id = request.data.get('category')
        status = request.data.get("status")
        video = request.data.get("video")
        
        topic = Topic.objects.get(id=topic)
        
        post_instance.title = title
        if picture != "undefined":
            post_instance.image=image
        post_instance.description=description
        post_instance.comment=comment
        post_instance.tags=tags     
        post_instance.category = category   
        post_instance.status=status_value
        if video != "undefined":
            post_instance.video=video
        
        post_instance.save()
    
        return Response({"message": "post updated successfully"},status=status.HTTP_200_OK)






# class EventListCreateView(generics.ListCreateAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer





# class TodoListView(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

#     def get_queryset(self):
#         user_id = self.kwargs['user_id']
#         user = User.objects.get(id=user_id)

#         todo = Todo.objects.filter(user=user) 
#         return todo
    

# class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = TodoSerializer

#     def get_object(self):
#         user_id = self.kwargs['user_id']
#         todo_id = self.kwargs['todo_id']

#         user = User.objects.get(id=user_id)
#         todo = Todo.objects.get(id=todo_id, user=user)

#         return todo
    

# class TodoMarkAsCompleted(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = TodoSerializer

#     def get_object(self):
#         user_id = self.kwargs['user_id']
#         todo_id = self.kwargs['todo_id']

#         user = User.objects.get(id=user_id)
#         todo = Todo.objects.get(id=todo_id, user=user)

#         todo.completed = True
#         todo.save()

#         return todo