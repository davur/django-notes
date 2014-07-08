from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework import viewsets

import django_filters


# Create your views here.

from .models import Tag, Note
from .permissions import IsOwnerOrReadOnly
from .serializers import NoteSerializer, TagSerializer, UserSerializer


class MainPageView(TemplateView):
    template_name = "index.html"



class NoteFilter(django_filters.FilterSet):
    tag = django_filters.CharFilter(name="tags__title")
    tag_id = django_filters.CharFilter(name="tags__id")

    class Meta:
        model = Note
        fields = ['title', 'tag', 'tag_id']


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_class = NoteFilter
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    filter_fields = ('tags__title',)

    def pre_save(self, obj):
        obj.owner = self.request.user

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (DjangoModelPermissions,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (DjangoModelPermissions,)
