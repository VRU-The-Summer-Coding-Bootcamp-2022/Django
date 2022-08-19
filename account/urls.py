from django.contrib import admin
from django.urls import path
from .views import handle_req
urlpatterns = [
    path('<int:pk>/', handle_req),
]
