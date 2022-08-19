
from django.shortcuts import render
from django.http import HttpResponse

from notepad.serializers import CreateNoteSerilizer, ListNoteSerilizer
from .models import Note
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.


def handle_req(request, pk):
    note: Note = Note.objects.get(id=pk)
    content = f'<h1>{note.id} - {note.title}</h1>'
    return HttpResponse(content)


class CreateNote(CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CreateNoteSerilizer


create_note_view = CreateNote.as_view()


class ListNote(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ListNoteSerilizer

    def get_queryset(self):
        return Note.objects.filter(person=self.request.user)


list_note_view = ListNote.as_view()
