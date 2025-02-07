from django.db import models

# from django.contrib.auth.base_user import BaseUserManager
# from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from django.urls import reverse
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives
# from django.utils.html import strip_tags
from django.db import models



from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.utils.html import mark_safe
from django.utils.text import slugify
from shortuuid.django_fields import ShortUUIDField
import shortuuid
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils import timezone
   



from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):

    first_name = None  # Tell Django this field doesn't exist
    last_name = None
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    # otp = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        email_username, mobile = self.email.split("@")
        if not self.full_name:
            self.full_name = email_username
        if not self.username:
            self.username = email_username
        super(CustomUser, self).save(*args, **kwargs)
    
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)



class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.FileField(upload_to="image", default="default/default-user.jpg", null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    # about = models.TextField(null=True, blank=True)
    # author = models.BooleanField(default=False)
    # country = models.CharField(max_length=100, null=True, blank=True)
    # facebook = models.CharField(max_length=100, null=True, blank=True)
    # twitter = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        if self.full_name:
            return str(self.full_name)
        else:
            return str(self.user.full_name)
    

    def save(self, *args, **kwargs):
        if self.full_name == "" or self.full_name == None:
            self.full_name = self.user.full_name
        super(Profile, self).save(*args, **kwargs)

    def thumbnail(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" object-fit:"cover" style="border-radius: 30px; object-fit: cover;" />' % (self.image))
    

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=CustomUser)
post_save.connect(save_user_profile, sender=CustomUser)



# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Email is a required field')
        
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractUser):
#     # full_name = models.CharField(max_length= 100, null= True,blank=True)
#     email = models.EmailField(max_length=200, unique=True)
#     # birthday = models.DateField(null=True,blank=True)
#     # username=models.CharField(max_length=200,null=True,blank=True)
    

#     objects=CustomUserManager()
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
    
#     def __str__(self):
#         return self.email
    
#     def save(self, *args, **kwargs):
#         mailusername, mobile = self.email.split("@")
#         if self.fullname == "" or self.fullname == None:
#             self.fullname = mailusername
#         if self.username == "" or self.username == None:
#             self.username = mailusername  
    
#         super(CustomUser, self).save(*args, **kwargs)

#     groups = models.ManyToManyField(
#         Group, 
#         related_name='customuser_groups',  # Custom reverse relation
#         blank=True
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='customuser_permissions',  # Custom reverse relation
#         blank=True
#     )
        


class Emails(models.Model):
    subject = models.CharField(max_length = 500)
    message = models.TextField(max_length = 500)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.id
        

# @receiver(reset_password_token_created)
# def password_reset_token_created(reset_password_token, *args, **kwargs):
#     sitelink = "http://localhost:5173/"
#     token = "{}".format(reset_password_token.key)
#     full_link = str(sitelink)+str("password=reset/")+str(token)

#     print (token)
#     print(full_link)

#     context = {
#         'full_link': full_link,
#         'email_address': reset_password_token.user.email

#     }
#     html_message = render_to_string("backend/email.html", context=context)
#     plain_message = strip_tags(html_message)

#     msg = EmailMultiAlternatives(
#     subject="Request for resetting password for {title}".format(title=reset_password_token.user.email),
#     body=plain_message,
#     from_email="sender@example.com",
#     to=[reset_password_token.user.email]
#     )


#     msg.attach_alternative(html_message, "text/html")
#     msg.send()


# class Profile(models.Model):
#         user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#         full_name = models.CharField(max_length=1000)
#         bio = models.CharField(max_length=100)
#         image = models.ImageField(upload_to="user_images", default="default.jpg")
#         verified = models.BooleanField(default=False)

#         def __str__(self):
#             return self.full_name


# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


# class Todo(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     title = models.CharField(max_length=1000)
#     completed = models.BooleanField(default=False)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title[:30]


class ChatMessage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user")
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="receiver")

    message = models.CharField(max_length=1000)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
        verbose_name_plural = "Messages"

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.message[:30]}"

    @property
    def sender_profile(self):
        profile, created = Profile.objects.get_or_create(user=self.sender)
        return profile

    @property
    def receiver_profile(self):
        profile, created = Profile.objects.get_or_create(user=self.receiver)
        return profile
    


class Category(models.Model):
        title = models.CharField(max_length=100)
        image = models.FileField(upload_to="image", null=True, blank=True)
        slug = models.SlugField(unique=True, null=True,blank=True)

        def __str__(self):
            return self.title
        
        class Meta:
            verbose_name_plural = "Category"


        def save(self, *args, **kwargs):
            if self.slug == "" or self.slug == None:
                self.slug = slugify(self.title)
            super(Category, self).save(*args, **kwargs)

        def post_count(self):
            return Post.objects.filter(category=self).count()

class Post(models.Model):
    STATUS = ( 
        ("Active", "Active"), 
        ("Draft", "Draft"),
        ("Disabled", "Disabled"),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to="image", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    status = models.CharField(max_length=100, choices=STATUS, default="Active")
    view = models.IntegerField(default=0)
    likes = models.ManyToManyField(CustomUser, blank=True, related_name="likes_user")
    slug = models.SlugField(unique=True, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Post"

    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title) + "-" + shortuuid.uuid()[:2]
        super(Post, self).save(*args, **kwargs)
    
    def comments(self):
        return Comment.objects.filter(post=self).order_by("-id")




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comment = models.TextField()
    reply = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} - {self.name}"
    
    class Meta:
        verbose_name_plural = "Comment"



# class Bookmark(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.post.title} - {self.user.username}"
    
#     class Meta:
#         verbose_name_plural = "Bookmark"





# class Notification(models.Model):
#     NOTI_TYPE = ( ("Like", "Like"), ("Comment", "Comment"), ("Bookmark", "Bookmark"))
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     type = models.CharField(max_length=100, choices=NOTI_TYPE)
#     seen = models.BooleanField(default=False)
#     date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = "Notification"
    
#     def __str__(self):
#         if self.post:
#             return f"{self.type} - {self.post.title}"
#         else:
#             return "Notification"



            