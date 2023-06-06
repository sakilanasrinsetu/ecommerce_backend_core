
from django.db import models

from base.models import BaseModel
from utils.generates import unique_slug_generator
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save

# Create your models here.


class Blog(BaseModel):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=230, unique=True)
    description = models.TextField()
    image = models.URLField()
    ordering = models.PositiveIntegerField(default=0)
    translation = models.JSONField(default=dict)

    class Meta:
        indexes = [
            models.Index(fields=["-created_at"]),
            models.Index(fields=["ordering"]),
        ]

    def __str__(self):
        return self.title

# ..........***.......... Blog ..........***..........


def blog_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = slugify(instance.title.lower()[:17])
        slug_binding = title + '-' + unique_slug_generator()
        instance.slug = slug_binding


pre_save.connect(blog_slug_pre_save_receiver, sender=Blog)