from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from knox.models import AuthToken
from django.shortcuts import render
from api.auth_backend import EmailAuthBackend
from .serializers import LoginSerializer, RegisterSerializer
from .serializers import *
from .models import *
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from .models import Emails
from rest_framework.views import APIView
from .pusher import pusher_client
from rest_framework import status
from rest_framework import generics



User = get_user_model()


def index(request):
    return render(request, 'gallery.jsx')



class MessageAPIView(APIView):
    def get(self, request):
        # Example: Return a success message for testing the GET method
        return Response({"message": "GET method is working!"}, status=200)

    def post(self, request):
        # Trigger a Pusher event with the provided username and message
        pusher_client.trigger('chat', 'message', {
            'username': request.data.get('username'),
            'message': request.data.get('message'),
        })
        return Response({"message": "Message sent!"}, status=201)
    
    
class LoginVViewset(viewsets.ViewSet):
    permission_classes =[permissions.AllowAny]
    serializer_class = LoginSerializer
    
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email=serializer.validated_data['email']
            password = serializer.validated_data['password']

            authen = EmailAuthBackend
            
            user=authen.authenticate(self,email=email, password=password)
            
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


class RegisterViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            _, token = AuthToken.objects.create(user)
            return Response({
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                },
                "token": token
            })
        else:
            return Response(serializer.errors, status=400)



class UserViewSet(viewsets.ReadOnlyModelViewSet):  # Use ReadOnlyModelViewSet for listing data
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RegisterSerializer
    queryset = User.objects.all()  # Define queryset at the class level

    def list(self, request):
        # You can further filter the queryset or add pagination if needed
        queryset = User.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = User.objects.get(id=user_id)

        todo = Todo.objects.filter(user=user) 
        return todo
    

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer

    def get_object(self):
        user_id = self.kwargs['user_id']
        todo_id = self.kwargs['todo_id']

        user = User.objects.get(id=user_id)
        todo = Todo.objects.get(id=todo_id, user=user)

        return todo
    

class TodoMarkAsCompleted(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer

    def get_object(self):
        user_id = self.kwargs['user_id']
        todo_id = self.kwargs['todo_id']

        user = User.objects.get(id=user_id)
        todo = Todo.objects.get(id=todo_id, user=user)

        todo.completed = True
        todo.save()

        return todo