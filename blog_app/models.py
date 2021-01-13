from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    text = models.CharField(max_length=300)
    post_image = models.ImageField(upload_to='post_images/')
