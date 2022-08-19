from django.shortcuts import render
from django.http import HttpResponse
from .models import MyUser
from notepad.models import Note
# Create your views here.


def handle_req(request, pk):
    user = MyUser.objects.get(id=pk)
    notes: Note = user.note_set.all()
    content = ''
    for note in notes:
        content += f'<h1>{note.id} - {note.title}</h1>'
    return HttpResponse(content)
