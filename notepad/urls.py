from django.contrib import admin
from django.urls import path
from .views import handle_req, create_note_view, list_note_view
urlpatterns = [
    path('<int:pk>/', handle_req),
    path('create/', create_note_view),
    path('all/', list_note_view),
]
