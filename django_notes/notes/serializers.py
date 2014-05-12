from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Note, Tag


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    tags = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                 view_name='tag-detail')

    class Meta:
        model = Note
        fields = ('url', 'owner', 'title', 'content_raw', 'tags',)


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'title',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    notes = serializers.HyperlinkedRelatedField(view_name='note-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'notes')
