from .models import Note
from rest_framework import serializers


class CreateNoteSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title','text']

    def create(self, validated_data):
        note = Note.objects.create(
            person=self.context['request'].user,
            **validated_data
        )
        note.save()
        return note


class ListNoteSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
