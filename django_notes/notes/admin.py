from django.contrib import admin
from django import forms
from pagedown.widgets import AdminPagedownWidget
from notes.models import Tag, Note

class TagAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )
    fieldsets = (
        (
            None,
            {
                'fields': ('title',)
            }
        ),
    )

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        widgets = {
            'content_raw' : AdminPagedownWidget(),
        }

class NoteAdmin(admin.ModelAdmin):
    form = NoteForm
    list_display = ('owner', 'title', 'date_modified')
    search_fields = ('owner', 'title', 'content_raw',)
    list_filter = ('tags',)
    fieldsets = (
        (
            None,
            {
                'fields': ('owner', 'title', 'content_raw', 'tags', )
            }
        ),
    )

admin.site.register(Tag, TagAdmin)
admin.site.register(Note, NoteAdmin)
