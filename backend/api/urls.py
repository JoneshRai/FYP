from django.urls import path
from django.contrib import admin 
from .views import * 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

# Initialize the router
router = DefaultRouter()
router.register('register', RegisterViewset, basename='register')
router.register('login', LoginVViewset, basename='login')
router.register('User', UserViewSet, basename='User')

# Define urlpatterns
urlpatterns = [
    path('messages', MessageAPIView.as_view()),  # Add MessageAPIView to urlpatterns
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/<user_id>/', ProfileView.as_view(), name='profile'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    
    path('Post/category/list/', CategoryListAPIView.as_view()),
    path('Post/category/posts/<category_slug>/', PostCategoryListAPIView.as_view()),
    
    ]+ router.urls 
