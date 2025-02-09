
from django.contrib import admin 
from .views import * 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path, include

# Initialize the router

# router.register('login', LoginViewset, basename='login')
# router.register('User', UserViewSet, basename='User')

# Define urlpatterns
urlpatterns = [

    

    # Userauths API Endpoints
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/register/', RegisterViewset.as_view(), name='auth_register'),
    path('user/profile/<user_id>/', ProfileView.as_view(), name='user_profile'),
    # path('user/password-reset/<email>/', PasswordEmailVerify.as_view(), name='password_reset'),
    # path('user/password-change/', PasswordChangeView.as_view(), name='password_reset'),

   
    # path('messages', MessageAPIView.as_view()),  # Add MessageAPIView to urlpatterns
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('profile/<user_id>/', ProfileView.as_view(), name='profile'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    
    path('post/category/list/', CategoryListAPIView.as_view()),
    path('Post/category/posts/<category_slug>/', PostCategoryListAPIView.as_view()),
    path('postlist/',PostListAPIView.as_view(),name='postList'),
    path('postdetail/<slug>/',PostDetailAPIView.as_view(),name='postdetail'),
    path('likepost/',LikePostAPIView.as_view(),name='like'),
    path('viewcomment/',ViewComment.as_view(),name='comment'),


    # for dashboard
    # path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('Dashboard/stats/<user_id>/',Dashboard.as_view(),name='Dashboard'),
     path('Dashboard/post-list/<user_id>/',DashboardPostlist.as_view(),name='DashboardPostlist'),
    path('DashboardCommentList/<user_id>/',DashboardCommentList.as_view(),name='DashboardCommentList'),
    path('DashboardCommentReply/<user_id>/',DashboardCommentReply.as_view(),name='DashboardCommentReply'),
    path('DashboardPostCreate/',DashboardPostCreate.as_view(),name='DashboardPostCreate'),
    path('DashboardUpdatePost/',DashboardUpdatePost.as_view(),name='DashboardUpdatePost'),
    
    ]
    # + router.urls 
