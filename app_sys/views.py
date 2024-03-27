from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .models import Note
from .forms import AddNoteForm

# Create your views here.

class NotesListView(ListView):
    model = Note
    template_name = 'app_sys/notes-list.html'
    context_object_name = 'notes'


class NotesDetailView(DetailView):
    model = Note
    template_name = 'app_sys/note-detail.html'
    context_object_name = 'note'


def add_note(request):
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('notes-list')
    else:
        form = AddNoteForm()

    return render(
        request,
        'app_sys/add-note.html',
        {'form': form}
    )