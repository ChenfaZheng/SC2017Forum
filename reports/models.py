import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Report(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False, 
    )
    title = models.CharField(max_length=200)
    reporter = models.CharField(max_length=200)
    abstract = models.CharField(max_length=2000)
    note = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
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
        return reverse("report_detail", args=[str(self.id)])
    