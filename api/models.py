from django.db import models
from utils.codec import Codec


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.CharField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = Codec.encode(self.password)
        super().save(*args, **kwargs)
