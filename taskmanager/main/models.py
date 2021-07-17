from django.db import models


class Note(models.Model):
    title = models.CharField('Head', max_length=50)
    note = models.TextField('Note')

    def __str__(self):
        return self.title
