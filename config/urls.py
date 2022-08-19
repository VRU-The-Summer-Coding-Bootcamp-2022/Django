from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('note/', include('notepad.urls')),
    path('user/', include('account.urls')),
    path('api-auth/', obtain_auth_token),
]
