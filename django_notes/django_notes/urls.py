from django.conf.urls import patterns, include, url
from django.contrib import admin

from notes.views import NoteViewSet, TagViewSet


from rest_framework.routers import DefaultRouter


admin.autodiscover()

router = DefaultRouter()
router.register(r'notes', NoteViewSet)
router.register(r'tags', TagViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_notes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(router.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
