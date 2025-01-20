from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model 
from api.models import  Todo,ChatMessage,Profile,CustomUser

# Get the user model
User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop('password', None)  
        return ret

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'user','full_name','image']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # Get the token from the parent class
        token = super().get_token(user)

        # Add custom claims to the token
        token['fullname'] = user.fullname
        token['email'] = user.email
        token['username'] = user.username

        return token
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self,validated_data):
        user = User.objects.create_user(
            username =validated_data['username'],
            email=validated_data['email'],
        )
        
        mailusername , mobile=user.email.split("@")
        user.username = mailusername
        user.set_password(validated_data['password'])
        user.save()
        return user 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields="__all__"
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields="__all__"



class CategorySerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    def get_post_count(self, category):
        return category.posts.count()
    
    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "image",
            "slug",
            "post_count",
        ]

    def __init__(self, *args, **kwargs):
        super(CategorySerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3








class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(CommentSerializer,self).__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.method =="POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1




class PostSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Post
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(PostSerializer,self).__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.method =="Post":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1



class AuthorSerial(serializers.Serializer):
    views = serializers.IntegerField(default=0)
    posts = serializers.IntegerField(default=0)
    likes = serializers.IntegerField(default=0)
    
    



class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ['id', 'user', 'title', 'completed']


class MessageSerializer(serializers.ModelSerializer):
    reciever_profile = ProfileSerializer(read_only=True)
    sender_profile = ProfileSerializer(read_only=True)

    class Meta:
        model = ChatMessage
        fields = ['id', 'user','sender','sender_profile', 'reciever','reciever_profile','message', 'is_read','date']
