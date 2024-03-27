from django.urls import path
from .views import NotesListView, NotesDetailView, add_note

urlpatterns = [
    path('', NotesListView.as_view(), name='notes-list'),
    path('note/<int:pk>', NotesDetailView.as_view(), name='note-detail'),
    path('add-note/', add_note, name='add-note')
]