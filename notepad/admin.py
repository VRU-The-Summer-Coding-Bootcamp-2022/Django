from django.contrib import admin
from .models import Note
# Register your models here.


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'text',
        'date',
        'person',
    ]
    sortable_by = [
        'id',
        'date',
        'person',
    ]
    search_fields = ['title']
