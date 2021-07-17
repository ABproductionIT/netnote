from .models import Note
from django.forms import ModelForm, TextInput, Textarea


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["title", "note"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Head'
            }),
            "note": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Note'
            }),
        }
