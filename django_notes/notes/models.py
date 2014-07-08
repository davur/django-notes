from django.db import models
from django.utils.translation import ugettext as _
import datetime

import markdown




class Tag(models.Model):
    """Tag Model"""
    class Meta:
        ordering = ['title',]

    title = models.CharField(
        max_length = 255
    )

    def __unicode__(self):
        return "%s" % (self.title,)


class Note(models.Model) :
    """Note Model"""
    class Meta:
        ordering = ['-date_modified']

    owner = models.ForeignKey(
        'auth.User',
        related_name='notes',
        verbose_name = _(u'Owner'),
        help_text = _(u' '),
    )
    title = models.CharField(
        verbose_name = _(u'Title'),
        help_text = _(u' '),
        max_length = 255
    )
    content_raw = models.TextField(
        verbose_name = _(u'Content (Markdown)'),
        help_text = _(u' '),
    )
    content_html = models.TextField(
        verbose_name = _(u'Content (HTML)'),
        help_text = _(u' '),
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name = _(u'Tags'),
        help_text = _(u' '),
        null = True,
        blank = True
    )
    date_created = models.DateTimeField(
      editable=False
    )
    date_modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date_created = datetime.datetime.today()
        self.date_modified = datetime.datetime.today()
        self.content_html = markdown.markdown(self.content_raw,
                                               extensions=["tables", "codehilite"],
                                               safe_mode=True)
        super(Note, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" % (self.title,)
