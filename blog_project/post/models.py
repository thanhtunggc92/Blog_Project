from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=255)
    intro=models.TextField()
    body=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    date_added=models.DateTimeField(auto_now_add=True)
    update_added=models.DateTimeField(auto_now=True)

    class Meta:
        ordering= ['-date_added']

    def __str__(self):
        return str(self.title)