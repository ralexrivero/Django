from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Notes
from .forms import NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class NotesDitailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/single_note.html"


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm


class NoteUpdateView(UpdateView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/single_note.html"
