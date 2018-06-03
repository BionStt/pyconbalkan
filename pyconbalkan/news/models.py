from django.db import models
from django.utils import timezone

from pyconbalkan.core.models import ActiveModel


class Post(ActiveModel):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='static/img/news', null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return '{} by {}'.format(self.title, self.author.username)