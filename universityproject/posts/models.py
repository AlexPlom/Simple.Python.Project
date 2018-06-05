from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=2000)
    createdAt = models.DateTimeField(default=datetime.now,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
