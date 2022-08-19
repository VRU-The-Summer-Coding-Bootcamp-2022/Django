from django.db import models

# Create your models here.


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    person = models.ForeignKey(
        'account.Myuser', models.DO_NOTHING, db_column='person')

    def __str__(self) -> str:
        return f'{self.id} - {self.title}'

    class Meta:
        db_table = 'notepad_note'
