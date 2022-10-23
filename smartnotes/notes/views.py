from django.shortcuts import render
from django.http import Http404

from .models import Notes

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def single_note(request, note_id):
    try:
        note = Notes.objects.get(pk=note_id)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/single_note.html', {'note': note})
