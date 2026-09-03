from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField()
    rate = models.IntegerField()
    is_published = models.BooleanField(default=False)