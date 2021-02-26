from django.db import models
from accounts.models import User
from django.utils import timezone




class Post(models.Model):
    master_username = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=5000, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    add_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
