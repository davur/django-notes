from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework import viewsets

# Create your views here.

from .models import Tag, Note
from .permissions import IsOwnerOrReadOnly
from .serializers import NoteSerializer, TagSerializer, UserSerializer


class MainPageView(TemplateView):
    template_name = "index.html"


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

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
