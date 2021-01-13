from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    text = models.TextField()
    post_image = models.ImageField(upload_to='post_images/')
