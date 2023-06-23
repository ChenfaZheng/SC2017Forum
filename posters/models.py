from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.urls import reverse
from uuid import uuid4
from pathlib import Path
import os
from django.utils.deconstruct import deconstructible

# Create your models here.


@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path
  
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            filename = '{}.{}'.format(uuid4().hex, ext)
            print(filename)
        return os.path(self.path, filename)


posters_path_gen = PathAndRename('posters/')


class Poster(models.Model):
    
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False, 
    )
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='posters/',  
        blank=True, 
        help_text='jpg or png format, suggest 1440x2560 (width x height in pixel)', 
#         height_field=str(2560), 
#         width_field=str(1440), 
    )

    uploader = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        default=None,
    )


    class Meta:
        permissions = [
            ('is_starchaser2017', 'Is StarChaser2017 Member'),
        ]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("poster_detail", args=[str(self.id)])
    
    def get_image_url(self):
        return self.image.url
    
