from rest_framework import serializers

from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model 

User = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    # Define a custom method to get the token for a user
    def get_token(cls, user):
        # print("User class:", user.__class__) 
        # Call the parent class's get_token method
        token = super().get_token(user)

        # Add custom claims to the token
        token['full_name'] = user.get_full_name() 
        token['email'] = user.email
        token['username'] = user.username
        # try:
        #     token['vendor_id'] = user.vendor.id
        # except:
        #     token['vendor_id'] = 0

        # ...

        # Return the token with custom claims
        return token




# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

#     def to_representation(self, instance):
#         ret = super().to_representation(instance)
#         ret.pop('password', None)  
#         return ret

# class ProfileSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Profile
#         fields = ['id', 'user','full_name','image']





class RegisterSerializer(serializers.ModelSerializer):
    # Define fields for the serializer, including password and password2
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        # Specify the model that this serializer is associated with
        model = CustomUser
        # Define the fields from the model that should be included in the serializer
        fields = ('full_name', 'email',  'password', 'password2')

    def validate(self, attrs):
        # Define a validation method to check if the passwords match
        if attrs['password'] != attrs['password2']:
            # Raise a validation error if the passwords don't match
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        # Return the validated attributes
        return attrs

    def create(self, validated_data):
        # Define a method to create a new user based on validated data
        user = CustomUser.objects.create(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
        )
        email_username, mobile = user.email.split('@')
        user.username = email_username

        # Set the user's password based on the validated data
        user.set_password(validated_data['password'])
        user.save()

        # Return the created user
        return user
    

class LoginSerializer(serializers.Serializer):
    email= serializers.EmailField()
    password = serializers.CharField()
    
    def to_representation(self,instance):
        ret = super().to_representation(instance)
        ret.pop('password',None)
        return ret

# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         # Get the token from the parent class
#         token = super().get_token(user)

#         # Add custom claims to the token
#         token['fullname'] = user.fullname
#         token['email'] = user.email
#         token['username'] = user.username

#         return token
        
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self,validated_data):
#         user = User.objects.create_user(
#             username =validated_data['username'],
#             email=validated_data['email'],
#         )
        
#         mailusername , mobile=user.email.split("@")
#         user.username = mailusername
#         user.set_password(validated_data['password'])
#         user.save()
#         return user 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
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
    comments = CommentSerializer(many=True)

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
    
    




# class EventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Event
#         fields = '__all__'

# class TodoSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Todo
#         fields = ['id', 'user', 'title', 'completed']


# class MessageSerializer(serializers.ModelSerializer):
#     reciever_profile = ProfileSerializer(read_only=True)
#     sender_profile = ProfileSerializer(read_only=True)

#     class Meta:
#         model = ChatMessage
#         fields = ['id', 'user','sender','sender_profile', 'reciever','reciever_profile','message', 'is_read','date']
