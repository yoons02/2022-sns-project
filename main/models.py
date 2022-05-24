from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    ...
    writer=models.ForeignKey(User,on_delete=models.CASCADE)

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to = "post/", blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]