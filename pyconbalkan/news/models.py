from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.utils.text import slugify

from pyconbalkan.core.models import ActiveModel


class Post(ActiveModel):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextField()
    keywords = TaggableManager()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='posts/image')
    slug = models.CharField(unique=True, blank=True, max_length=100)
    front_page = models.BooleanField("Promote news article to frontpage", default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return '{} by {}'.format(self.title, self.author.username)

    class Meta:
        ordering = ("-published_date",)
