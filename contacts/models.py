from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    # Link each contact to a User. If a user is deleted, all their contacts are also deleted.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True) # blank=True means this field is optional
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name