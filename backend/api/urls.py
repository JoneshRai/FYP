from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MessageAPIView, RegisterViewset, LoginVViewset, UserViewSet

# Initialize the router
router = DefaultRouter()
router.register('register', RegisterViewset, basename='register')
router.register('login', LoginVViewset, basename='login')
router.register('User', UserViewSet, basename='User')

# Define urlpatterns
urlpatterns = [
    path('messages', MessageAPIView.as_view()),  # Add MessageAPIView to urlpatterns
]

# Include router-generated URLs
urlpatterns += router.urls
