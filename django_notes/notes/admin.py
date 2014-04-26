from django.contrib import admin
from django import forms
from pagedown.widgets import AdminPagedownWidget
from notes.models import Tag, Note

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', )
    search_fields = ('title', )
    fieldsets = (
        (
            None,
            {
                'fields': ('title', 'slug',)
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
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'date_modified')
    search_fields = ('title', 'content_raw',)
    list_filter = ('tags',)
    fieldsets = (
        (
            None,
            {
                'fields': ('title', 'slug', 'content_raw', 'tags', )
            }
        ),
    )

admin.site.register(Tag, TagAdmin)
admin.site.register(Note, NoteAdmin)
