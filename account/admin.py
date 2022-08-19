from django.contrib import admin

from notepad.models import Note
from .models import MyUser
# Register your models here.


class NoteInlines(admin.StackedInline):
    model = Note


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):

    inlines = [NoteInlines]
