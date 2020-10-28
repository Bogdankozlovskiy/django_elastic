from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(default='', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
# Create your models here.
