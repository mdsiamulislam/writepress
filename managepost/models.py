from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
