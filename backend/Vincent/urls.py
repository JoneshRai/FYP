from django.contrib import admin
from django.urls import path, include
from knox import views as knox_views
from django.conf import settings
from django.conf.urls.static import static


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Blog Backend APIs",
        default_version="v1",
        description="This is the documentation for the backend API",
        terms_of_service="http://mywbsite.com/policies/",
        contact=openapi.Contact(email="desphixs@gmail.com"),
        license=openapi.License(name="BSD Licence"),
    ),
    public=True,
    permission_classes = (permissions.AllowAny, )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include ('api.urls')),
    path('api/auth/',include('knox.urls')),
    path('api/password_reset/', include ('django_rest_passwordreset.urls', namespace='password_reset')),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_resets')),
    


   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




