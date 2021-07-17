from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm


def index(request):
    error = ''
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connect')
        else:
            error = "error"

    form = NoteForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/index.html', context)


def about(request):
    notes = Note.objects.order_by('id')
    return render(request, 'main/about.html', {'notes': notes})


def connect(request):
    notes = Note.objects.order_by('-id')
    return render(request, 'main/connect.html', {'notes': notes})
